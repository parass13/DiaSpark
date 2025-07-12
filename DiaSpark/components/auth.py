# components/auth.py

from utils.db import sign_up_user, login_user, supabase
import gradio as gr

def register(email, password, gender, username):
    """Handler for the signup process, now including username."""
    if not all([email, password, gender, username]):
        return "❌ All fields are required.", gr.update(), gr.update(), gr.update(), gr.update()
    
    result = sign_up_user(email, password, gender, username)

    if result and result.user:
        message = "✅ Signup successful! You can now log in."
        if result.user and not result.session:
             message = "✅ Signup successful! Please check your email to confirm your account."
        # On success, clear all four signup fields
        return message, "", "", None, ""
    
    if hasattr(result, 'error') and result.error:
        # Check for unique constraint violation on username
        if 'duplicate key value violates unique constraint "users_username_key"' in result.error.message:
            return "❌ Signup Failed: This username is already taken.", gr.update(), gr.update(), gr.update(), gr.update()
        return f"❌ Signup Failed: {result.error.message}", gr.update(), gr.update(), gr.update(), gr.update()
    
    return "❌ Signup failed. An unknown error occurred.", gr.update(), gr.update(), gr.update(), gr.update()


def login(email, password, current_user_state):
    """Handler for login. Now fetches username and gender from the database."""
    if not email or not password:
        return "❌ Email and password cannot be empty.", current_user_state, gr.update()

    result = login_user(email, password)
    
    if result and result.session:
        try:
            # Fetch username and gender in a single query for efficiency
            profile = supabase.table("users").select("gender, username").eq("id", result.user.id).single().execute()
            user_gender = profile.data.get("gender") if profile.data else None
            user_name = profile.data.get("username") if profile.data else "User"
        except Exception as e:
            print(f"Could not fetch user profile: {e}")
            user_gender = None
            user_name = "User"

        # Add username to the user's session state
        new_user_state = {"email": email, "id": result.user.id, "logged_in": True, "gender": user_gender, "username": user_name}
        return f"✅ Welcome, {user_name}! Redirecting...", new_user_state, gr.Tabs(selected="prediction_tab")
    
    if hasattr(result, 'error') and result.error:
        return f"❌ Login Failed: {result.error.message}", current_user_state, gr.update()
    
    return "❌ Login failed. Check credentials or confirm your email.", current_user_state, gr.update()


def logout(current_user_state):
    """Handler for logout. Clears all state and form fields."""
    new_user_state = {"email": None, "id": None, "logged_in": False, "gender": None, "username": None}
    
    return (
        "👋 Logged out successfully.",              # 1. auth_message
        new_user_state,                         # 2. user_state
        gr.Tabs(selected="home_tab"),           # 3. main_tabs
        "",                                     # 4. email_login
        "",                                     # 5. pwd_login
        None,                                   # 6. preg
        None,                                   # 7. glucose
        None,                                   # 8. bp
        None,                                   # 9. insulin
        None,                                   # 10. bmi
        None,                                   # 11. age
        "",                                     # 12. result_output
        gr.update(visible=False),               # 13. pregnancies_row
        None,                                   # 14. weight (NEW)
        None,                                   # 15. height (NEW)
        None                                    # 16. bmi_choice (NEW)
    )