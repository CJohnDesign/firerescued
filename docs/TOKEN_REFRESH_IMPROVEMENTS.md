# Token Refresh Improvements

## Overview

The WHOOP token refresh system has been significantly improved to address token expiration issues and provide better automatic refresh functionality. This document outlines the changes made and how to test them.

## Key Improvements

### 1. **Real Expiration Checking** ✅
- **Before**: Used a manual `is_valid` flag that was often not set correctly
- **After**: Calculates actual expiration based on `created_at + expires_in` with a configurable buffer

```python
def is_token_expired(token_info):
    """Check if token is expired based on creation time and expires_in"""
    # Handles both Supabase (ISO) and SQLite (datetime) formats
    # Includes 10-minute buffer before expiration
    # Returns True if expired or will expire soon
```

### 2. **Proactive Token Refresh** ✅
- **Buffer Time**: Tokens are refreshed 10 minutes before they actually expire
- **Automatic Retry**: If refresh fails, falls back to potentially expired token
- **Better Error Handling**: Distinguishes between network errors and auth errors

### 3. **Enhanced Logging & Debugging** ✅
- **Detailed Logs**: Every token operation now includes comprehensive logging
- **Visual Indicators**: Uses emojis and clear formatting for easy debugging
- **Status Tracking**: Shows token creation time, expiration, and refresh attempts

### 4. **Improved Database Compatibility** ✅
- **Cross-Platform**: Works with both Supabase (ISO timestamps) and SQLite (datetime objects)
- **Timestamp Fields**: Both databases now return `created_at` and `updated_at` for expiration calculations

### 5. **New Helper Functions** ✅

#### `check_token_status(username="default")`
Returns detailed token status information:
```python
{
    "status": "valid|expired|missing|no_token",
    "message": "Human-readable status description",
    "has_access_token": bool,
    "has_refresh_token": bool,  
    "is_expired": bool,
    "expires_in": int,
    "created_at": str,
    "updated_at": str
}
```

#### `test_api_connectivity(username="default")`
Tests actual WHOOP API connectivity with current token:
- Returns `True` if API calls succeed
- Returns `False` if unauthorized or other errors
- Includes timeout handling

## Configuration

### Token Refresh Buffer
```python
# In app/services/whoop_service.py
TOKEN_REFRESH_BUFFER_MINUTES = 10  # Refresh 10 minutes before expiration
```

### Environment Variables Required
```bash
# WHOOP API credentials
WHOOP_CLIENT_ID=your_client_id
WHOOP_CLIENT_SECRET=your_client_secret
WHOOP_REDIRECT_URI=http://localhost:3000

# For Supabase users
SUPABASE_USER_ID=your_user_uuid
```

## Testing

### Automated Test Script
Run the included test script to verify functionality:

```bash
python test_token_refresh.py
```

This script will:
1. Check current token status
2. Test API connectivity
3. Verify token retrieval and refresh logic
4. Provide a summary report

### Manual Testing
1. **Check Token Status**: Call `check_token_status()` in your app
2. **Force Refresh**: Manually set token expiration to trigger refresh
3. **API Calls**: Make WHOOP API calls to test automatic refresh

## Expected Behavior

### Valid Token
```
🔐 === CHECKING ACCESS TOKEN ===
   - Username: default
   - Use Supabase: True
🔍 Token info from database:
   - Has access_token: True
   - Has refresh_token: True
   - Expires in: 3600 seconds
✅ Using valid token from database
```

### Expired Token with Refresh
```
🔐 === CHECKING ACCESS TOKEN ===
🔍 Token expiration check:
   - Created: 2024-01-15 10:00:00
   - Expires in: 3600 seconds
   - Effective expiry: 2024-01-15 10:50:00
   - Current time: 2024-01-15 11:00:00
   - Is expired: True
🔄 Token expired/expiring soon - attempting refresh
🔄 === REFRESHING ACCESS TOKEN ===
✅ Token refreshed successfully
```

### Failed Refresh Fallback
```
❌ Error refreshing token: Invalid refresh token
⚠️  Refresh failed - trying with potentially expired token
```

## Error Handling

### Graceful Degradation
- If refresh fails, attempts to use existing token
- Provides clear error messages for different failure scenarios
- Never crashes the application due to token issues

### Error Categories
1. **No Token**: User needs to re-authenticate via OAuth
2. **Expired Token + Valid Refresh**: Automatic refresh attempted
3. **Expired Token + Invalid Refresh**: User needs to re-authenticate
4. **Network Errors**: Temporary failures, retry recommended

## API Integration

### Automatic Integration
All WHOOP API calls now automatically:
1. Check token expiration before making requests
2. Refresh tokens if needed
3. Include proper error handling for 401 responses
4. Log detailed information for debugging

### Updated Functions
- `get_daily_recovery()` - Enhanced error handling
- `get_daily_strain()` - Enhanced error handling  
- `get_daily_sleep()` - Enhanced error handling
- `get_daily_workouts()` - Enhanced error handling

## Troubleshooting

### Common Issues

#### "No valid token available"
- **Cause**: No token in database or all tokens expired
- **Solution**: Re-authenticate via OAuth flow

#### "Error refreshing token: Invalid refresh token"
- **Cause**: Refresh token is expired or revoked
- **Solution**: Re-authenticate via OAuth flow

#### "Token expired/expiring soon - attempting refresh"
- **Normal**: This is the system working correctly
- **Action**: Monitor logs to ensure refresh succeeds

### Debug Mode
Enable detailed logging by running the test script:
```bash
python test_token_refresh.py
```

## Migration Notes

### Existing Users
- Existing tokens will continue to work
- First API call after upgrade will use new expiration logic
- Users with expired tokens will need to re-authenticate

### Database Schema
- No schema changes required
- New fields (`created_at`, `updated_at`) already existed
- SQLite `get_user_token()` now returns timestamp fields

## Next Steps

1. **Monitor Logs**: Watch for automatic refresh behavior in production
2. **User Education**: Inform users they may need to re-authenticate once
3. **Metrics**: Consider adding token refresh metrics to dashboard
4. **Notifications**: Add user-friendly notifications for re-authentication needs

## Files Modified

- `app/services/whoop_service.py` - Main token refresh logic
- `app/database/sqlite.py` - Updated token retrieval to include timestamps
- `test_token_refresh.py` - New test script
- `docs/TOKEN_REFRESH_IMPROVEMENTS.md` - This documentation

---

**Status**: ✅ **Implemented and Ready for Testing**

Run `python test_token_refresh.py` to verify the improvements are working in your environment. 