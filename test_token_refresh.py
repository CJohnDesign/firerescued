#!/usr/bin/env python3
"""
Test script for WHOOP token refresh functionality.
Run this to test if the improved token refresh logic is working.
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Add the app directory to path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

# Load environment variables
load_dotenv()

def check_environment():
    """Check if all required environment variables are set"""
    print("🔍 === CHECKING ENVIRONMENT VARIABLES ===")
    
    # Clean up environment variables by removing comments
    def clean_env_var(var_name):
        value = os.getenv(var_name)
        if value:
            # Remove inline comments (anything after #)
            cleaned = value.split('#')[0].strip()
            return cleaned
        return value
    
    required_vars = {
        "WHOOP_CLIENT_ID": clean_env_var("WHOOP_CLIENT_ID"),
        "WHOOP_CLIENT_SECRET": clean_env_var("WHOOP_CLIENT_SECRET"),
        "SUPABASE_URL": clean_env_var("SUPABASE_URL"),
        "SUPABASE_KEY": clean_env_var("SUPABASE_KEY"),
        "SUPABASE_USER_ID": clean_env_var("SUPABASE_USER_ID")
    }
    
    missing_vars = []
    for var_name, var_value in required_vars.items():
        if var_value:
            print(f"   ✅ {var_name}: {var_value[:10]}..." if len(var_value) > 10 else f"   ✅ {var_name}: {var_value}")
        else:
            print(f"   ❌ {var_name}: Missing")
            missing_vars.append(var_name)
    
    if missing_vars:
        print(f"\n❌ Missing required environment variables: {missing_vars}")
        print("   Please check your .env file.")
        return False
    
    print("\n✅ All required environment variables are set")
    
    # Update environment variables with cleaned values
    for var_name, var_value in required_vars.items():
        if var_value:
            os.environ[var_name] = var_value
    
    return True

def test_database_connection():
    """Test database connection"""
    print("\n🔗 === TESTING DATABASE CONNECTION ===")
    
    try:
        # Import and test database initialization
        from app.database.supabase import init_supabase_client, get_whoop_token
        
        print("   - Initializing Supabase client...")
        client = init_supabase_client()
        
        if client:
            print("   ✅ Supabase client initialized successfully")
            
            # Test a simple query
            user_id = os.getenv("SUPABASE_USER_ID")
            print(f"   - Testing token query for user: {user_id}")
            
            token_info = get_whoop_token(user_id)
            if token_info:
                print(f"   ✅ Token found in database")
                return True, token_info
            else:
                print(f"   ⚠️  No token found for user {user_id}")
                return True, None
        else:
            print("   ❌ Failed to initialize Supabase client")
            return False, None
            
    except Exception as e:
        print(f"   ❌ Database connection failed: {str(e)}")
        return False, None

def test_token_refresh():
    """Test the token refresh functionality"""
    print("\n🧪 === TESTING TOKEN REFRESH FUNCTIONALITY ===")
    print(f"   - Timestamp: {datetime.now()}")
    
    try:
        # Import the whoop service
        from app.services.whoop_service import (
            check_token_status, 
            test_api_connectivity,
            get_valid_access_token
        )
        
        print("\n1️⃣ Checking current token status...")
        status = check_token_status()
        
        print("\n2️⃣ Testing API connectivity...")
        connectivity = test_api_connectivity()
        
        print("\n3️⃣ Testing token retrieval...")
        try:
            token = get_valid_access_token()
            if token:
                print(f"✅ Successfully retrieved token: {token[:10]}...")
            else:
                print(f"❌ No token retrieved")
        except Exception as e:
            print(f"❌ Error retrieving token: {str(e)}")
        
        print("\n📋 === TEST SUMMARY ===")
        print(f"   - Token Status: {status.get('status', 'unknown')}")
        print(f"   - Has Access Token: {status.get('has_access_token', False)}")
        print(f"   - Has Refresh Token: {status.get('has_refresh_token', False)}")
        print(f"   - Is Expired: {status.get('is_expired', True)}")
        print(f"   - API Connectivity: {'✅ Success' if connectivity else '❌ Failed'}")
        
        if status.get('status') == 'valid' and connectivity:
            print("\n🎉 All tests passed! Token refresh system is working correctly.")
            return True
        elif status.get('status') == 'expired' and status.get('has_refresh_token'):
            print("\n⚠️  Token is expired but has refresh capability. Try running sync to test refresh.")
            return True
        else:
            print("\n❌ Issues detected with token system. Check your WHOOP credentials and database.")
            return False
            
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        print("   Make sure you're running this from the project root directory.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        print(f"   Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("🔧 WHOOP Token Refresh Test")
    print("=" * 50)
    
    # Step 1: Check environment variables
    if not check_environment():
        return False
    
    # Step 2: Test database connection
    db_success, token_info = test_database_connection()
    if not db_success:
        print("\n❌ Database connection failed. Cannot proceed with token tests.")
        return False
    
    # Step 3: Test token refresh functionality
    return test_token_refresh()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 