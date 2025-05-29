# Issue #001: Whoop Sync Returns "No Data" - Token Investigation

**Status:** Open  
**Type:** Research Spike  
**Priority:** High  
**Created:** 2024-12-19  
**Assignee:** TBD  

## Problem Statement

When users click the "Sync Now" button in the settings page, the application displays "No Whoop data available for [date]" message, suggesting that either:
1. The WHOOP API token has expired
2. The token authentication is failing
3. The API call is returning empty data sets
4. There's an issue with the token refresh mechanism

## Current Behavior

- User clicks "Sync Now" button on `/settings` page
- Application calls `/fetch_whoop_data` endpoint
- System reports "No Whoop data available for today"
- No sync data is retrieved or stored

## Technical Investigation Areas

### 1. Token Validation Chain
**File:** `app/services/whoop_service.py`
- Check `get_valid_access_token()` function (lines ~130-170)
- Review token refresh logic in `refresh_access_token()` 
- Verify `is_token_valid()` implementation

### 2. Token Storage & Retrieval
**Database Layer:**
- **Supabase:** `app/database/supabase.py` - `get_whoop_token()` and `save_whoop_token()`
- **SQLite:** `app/database/sqlite.py` - `get_user_token()` and `save_user_token()`

### 3. API Request Flow
**File:** `app/core/routes.py:395` - `manual_fetch_data()` function
- Verify user_id retrieval
- Check date parsing and validation
- Review the call to `get_all_daily_metrics()`

### 4. WHOOP API Authentication
**OAuth Flow:**
- Authorization URL generation (`get_auth_url()`)
- Token exchange (`get_token_from_code()`)
- Token refresh mechanism
- Headers construction (`get_headers()`)

## Debug Steps to Investigate

### Step 1: Token Verification
```bash
# Check if user has valid tokens in database
# Look for token expiration timestamps
# Verify access_token and refresh_token presence
```

### Step 2: API Response Analysis
```bash
# Add detailed logging to capture:
# - HTTP status codes from WHOOP API
# - Response headers and body
# - Token refresh attempts
# - Authentication errors
```

### Step 3: Environment Variable Check
```bash
# Verify WHOOP API credentials are properly set:
# - WHOOP_CLIENT_ID
# - WHOOP_CLIENT_SECRET  
# - WHOOP_REDIRECT_URI
# - SUPABASE_USER_ID (if using Supabase)
```

### Step 4: Manual Token Test
```bash
# Test token validity with direct API call
# Verify scopes: read:recovery, read:profile, read:cycles, read:sleep, read:workout, read:body_measurement
```

## Expected Outcomes

1. **Root Cause Identification**: Determine whether issue is token expiration, API changes, or configuration
2. **Fix Implementation**: Address the core authentication issue
3. **Improved Error Handling**: Better user messaging for token-related failures
4. **Monitoring**: Add token health checks and proactive refresh

## Related Files

- `app/services/whoop_service.py` - Core WHOOP API integration
- `app/core/routes.py` - Sync endpoint and error handling
- `app/database/supabase.py` - Token storage (Supabase)
- `app/database/sqlite.py` - Token storage (SQLite fallback)
- `app/templates/settings.html` - UI with sync button

## Potential Solutions

1. **Token Refresh Enhancement**: Improve automatic token refresh logic
2. **Better Error Handling**: Distinguish between expired tokens vs no data
3. **Token Health Dashboard**: Add token status to settings page
4. **Graceful Degradation**: Handle token issues without breaking sync flow

## Next Steps

1. [ ] Add comprehensive logging to token validation flow
2. [ ] Test token refresh mechanism manually
3. [ ] Verify WHOOP API endpoints are still valid
4. [ ] Check token expiration handling
5. [ ] Implement token health status indicator
6. [ ] Add retry logic for failed API calls

## Notes

- The error message "No Whoop data available for [date]" is triggered in `app/core/routes.py:448`
- Application supports both Supabase and SQLite token storage
- OAuth flow uses authorization code grant with refresh tokens
- Current token scopes include recovery, profile, cycles, sleep, workout, and body measurements 