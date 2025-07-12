# utils/db.py

import os
from supabase import create_client, Client

# Fetch Supabase credentials securely from environment variables/secrets
SUPABASE_URL = "YOUR_URL"
SUPABASE_KEY = "SUPABASE_KEY"



if not SUPABASE_URL or not SUPABASE_KEY:
    raise EnvironmentError("Supabase credentials (SUPABASE_URL, SUPABASE_KEY) are not set.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def sign_up_user(email, password, gender, username):
    """Signs up a new user, passing gender in the options metadata."""
    try:
        # The 'gender' is passed inside the 'options' dictionary.
        # This is how Supabase receives extra data during signup, which our trigger will then use.
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {
                    "gender": gender,
                    "username": username
                }
            }
        })
        return response
    except Exception as e:
        print(f"Error during sign up in utils.db: {e}")
        return None

def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return response
    except Exception as e:
        print(f"Error during login in utils.db: {e}")
        return None

def log_prediction(data, prediction_result, user_id):
    """Logs prediction data to the 'predictions' table using user_id."""
    try:
        prediction_value = 1 if "Diabetic" in prediction_result else 0
        response = supabase.table("predictions").insert({
            "pregnancies": data[0],
            "glucose": data[1],
            "blood_pressure": data[2],
            "insulin": data[3],
            "bmi": data[4],
            "age": data[5],
            "prediction": prediction_value,
            "user_id": user_id
        }).execute()
        
        if len(response.data) > 0:
            print("Prediction logged successfully.")
        else:
            print(f"Error logging prediction: Supabase returned no data. Possible error: {response.error}")
    except Exception as e:
        print(f"Error during prediction logging function: {e}")