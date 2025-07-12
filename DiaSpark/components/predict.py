# components/predict.py

import pickle
import numpy as np
from utils.db import log_prediction

try:
    model = pickle.load(open("model.pkl", "rb"))
except FileNotFoundError:
    raise RuntimeError("The 'model.pkl' file was not found.")

# The function signature is now simpler
def predict(pregnancies, glucose, blood_pressure, insulin, bmi, age, user_state):
    """
    Predicts diabetes risk using the final BMI value provided from the UI.
    """
    if not user_state.get("logged_in"):
        return "❌ Please log in first."

    # Use 0 for pregnancies if the field is hidden (male user)
    pregnancies_value = pregnancies if pregnancies is not None else 0
    
    # Check that all essential fields have a value
    if any(v is None for v in [glucose, blood_pressure, insulin, bmi, age]):
        return "❌ Please fill in all the required health fields, including BMI."
    
    # The 'bmi' value is now received directly, no calculation needed here
    input_data = [pregnancies_value, glucose, blood_pressure, insulin, bmi, age]
    data_np = np.array(input_data).reshape(1, -1)
    
    try:
        prediction = model.predict(data_np)[0]
        result_text = "Chances of having Diabetes , consult to the doctors!! " if prediction == 1 else "Congratulations, No chances of having Diabetes !!"
        final_result = f" {result_text}"
        
        # Log prediction if user ID exists
        if user_state.get("id"):
            log_prediction(input_data, result_text, user_state["id"])
        
        return final_result
    except Exception as e:
        return f"An error occurred during prediction: {e}"