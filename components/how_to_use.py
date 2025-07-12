# components/how_to_use.py

import gradio as gr

def render_how_to_use_guide():
    """
    Creates and returns the Gradio UI for the 'How to Use' guide.
    """
    with gr.Blocks() as guide_ui:
        gr.Markdown("## 💡 How to Use the Prediction Tool")
        gr.Markdown(
            "This guide helps you understand what each required value means and how you can find it. "
            "Accurate data leads to a more meaningful prediction."
        )
        gr.Markdown("---")

        with gr.Accordion("Glucose Level", open=True):
            gr.Markdown(
                """
                **What it is:** The amount of sugar in your blood. This is a key indicator for diabetes.
                **How to get it:**
                *   From a recent lab report (often called "Fasting Glucose" or "Plasma Glucose").
                *   Using a home blood glucose meter. For the most accurate prediction, a fasting level (before eating in the morning) is often best.
                **Unit:** mg/dL (milligrams per deciliter).
                """
            )

        with gr.Accordion("Blood Pressure", open=False):
            gr.Markdown(
                """
                **What it is:** The pressure of blood pushing against the walls of your arteries. We need the bottom number (Diastolic).
                **How to get it:**
                *   Using an automatic blood pressure cuff at home or at a pharmacy.
                *   From a reading taken at a doctor's office.
                **Unit:** The bottom number of your reading (e.g., if your reading is 120/80, you enter 80).
                """
            )
            
        with gr.Accordion("Insulin", open=False):
            gr.Markdown(
                """
                **What it is:** The level of insulin hormone in your blood.
                **How to get it:** This value is typically only available from a specific blood test ordered by a doctor, often called a "2-Hour Serum Insulin" test.
                **What if I don't know it?** If you don't have this value, you can enter `0`. The model can still make a prediction, but it will be more accurate if you can provide it.
                """
            )

        with gr.Accordion("BMI (Body Mass Index) or Weight/Height", open=False):
            gr.Markdown(
                """
                **What it is:** A measure of body fat based on your height and weight.
                **How to get it:**
                1.  **Option 1 (Direct):** If you already know your BMI from a doctor or an online calculator, you can enter it directly.
                2.  **Option 2 (Calculate):** If you don't know your BMI, the app can calculate it for you! Just provide your current weight in kilograms (kg) and your height in centimeters (cm).
                """
            )
        
        with gr.Accordion("Pregnancies (Females Only)", open=False):
            gr.Markdown(
                """
                **What it is:** The number of times you have been pregnant.
                **How to get it:** This is based on your personal medical history.
                **Note:** This field will only appear if you selected 'Female' during signup.
                """
            )