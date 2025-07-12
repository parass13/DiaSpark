import gradio as gr

def render_factors_info():
    """
    Creates and returns the Gradio UI for the 'Factors Affecting Diabetes' content.
    """
    with gr.Blocks() as factors_ui:
        gr.Markdown("## 🩺 Understanding the Factors Behind Diabetes")
        gr.Markdown(
            "Diabetes is a complex condition influenced by a mix of genetic, lifestyle, and environmental factors. "
            "Understanding your personal risk factors is the first step toward prevention and effective management."
        )
        gr.Markdown("---")

        with gr.Accordion("Type 2 Diabetes: The Most Common Form", open=True):
            gr.Markdown(
                """
                This occurs when your body becomes resistant to insulin or doesn't produce enough.
                
                ### Factors You Cannot Change (Non-Modifiable)
                *   **🧬 Family History:** A parent or sibling with Type 2 diabetes significantly increases your risk.
                *   **🗓️ Age:** Risk increases after age 35.
                *   **🌍 Race or Ethnicity:** People of certain backgrounds (African American, Hispanic, American Indian, Asian American) are at higher risk.
                *   **🤰 History of Gestational Diabetes:** If you had diabetes during a pregnancy, your risk is higher.
                ### Lifestyle-Related Risk Factors (Modifiable)
                *   **⚖️ Weight:** Being overweight or having obesity is the single most important risk factor.
                *   **🏃‍♀️ Physical Inactivity:** A sedentary lifestyle reduces your body's ability to use insulin.
                *   **🍔 Unhealthy Diet:** High consumption of processed foods, sugar, and unhealthy fats.
                *   **🩸 High Blood Pressure & Cholesterol:** These conditions are often linked to insulin resistance.
                *   **🚬 Smoking:** This habit increases inflammation and makes it harder for your body to manage blood sugar.
                """
            )

        with gr.Accordion("Type 1 Diabetes: An Autoimmune Condition", open=False):
            gr.Markdown(
                """
                This type occurs when the body's immune system mistakenly attacks and destroys the insulin-producing cells in the pancreas. The exact triggers are not fully known.
                
                ### Key Factors
                *   **🧬 Family History:** While not as strong as in Type 2, having a close relative with Type 1 increases risk.
                *   **🔬 Genetics:** Specific genes are known to make individuals more susceptible.
                *   **🎂 Age:** It is most commonly diagnosed in children, teens, and young adults.
                *   **🦠 Environmental Triggers:** It is believed that certain viruses might trigger the autoimmune attack in genetically predisposed individuals.
                """
            )

        with gr.Accordion("Gestational Diabetes: During Pregnancy", open=False):
            gr.Markdown(
                """
                This type of diabetes develops in some women during pregnancy and usually disappears after birth. However, it increases the risk for both mother and child to develop Type 2 diabetes later in life.
                
                ### Key Risk Factors
                *   **⚖️ Pre-pregnancy Weight:** Being overweight before becoming pregnant.
                *   **🗓️ Maternal Age:** Being older than 25.
                *   **👨‍👩‍👧 Family History:** A family history of Type 2 diabetes.
                *   **🩺 Medical History:** Having had gestational diabetes before or having Polycystic Ovary Syndrome (PCOS).
                """
            )