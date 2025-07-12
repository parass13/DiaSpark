# app.py

import gradio as gr
from components.auth import register, login, logout
from components.predict import predict
from components.report_generator import create_report
from components.diabetes_factors import render_factors_info
from components.food_suggestions import render_food_guide
from components.doctor_info import render_doctor_list
from components.how_to_use import render_how_to_use_guide

# app.py

import gradio as gr
from components.auth import register, login, logout
from components.predict import predict
from components.report_generator import create_report
from components.diabetes_factors import render_factors_info
from components.food_suggestions import render_food_guide
from components.doctor_info import render_doctor_list
from components.how_to_use import render_how_to_use_guide

# --- Style and Theme with  Mobile-Responsive CSS ---
css = """
/* --- CRITICAL FIX FOR SCROLLING ON MOBILE --- */
/* This forces the entire page to allow vertical scrolling and grow with its content */
html, body {
  overflow-y: auto !important; /* Allow vertical scrolling! */
  height: auto !important;     /* Let the body grow beyond the screen height */
}
/* General container style for all screens */
.gradio-container { max-width: 1000px !important; margin: auto !important; }
.centered-text { text-align: center; }
/* Fix for invisible button text in dark mode */
.gradio-button.primary, .gradio-button.secondary {
  color: white !important;
}
/* Responsive rules for stacking content WITHIN the app */
@media (max-width: 768px) {
  .gradio-row {
    flex-direction: column !important;
    gap: 1rem !important;
  }
  .gradio-row > * {
    width: 100% !important;
    min-width: unset !important;
    margin: 0 !important;
  }
}
"""
with gr.Blocks(title="DiaSpark: Your Health Management Platform", css=css) as demo:

    user_state = gr.State({"email": None, "id": None, "logged_in": False, "gender": None, "username": None})

    # --- Static Header (Always Visible) ---
    gr.Markdown("# 🩺 Welcome to DiaSpark: Your Health Management Platform")

    # --- Personalized Header (Visible only when logged in) ---
    with gr.Row(visible=False) as logged_in_header:
        welcome_message = gr.Markdown()

    # --- Main Tabs ---
    with gr.Tabs() as main_tabs:

        # --- Tab 1: Homepage ---
        with gr.TabItem("Home 🏠", id="home_tab"):
            gr.Markdown(
                "<h2 class='centered-text'>A Smart First Step in Understanding Your Health</h2>",
                elem_classes="centered-text"
            )
            gr.Markdown(
                """
                DiaSpark is a confidential tool that uses machine learning to provide an educational analysis of your diabetes risk factors.
                Our goal is to promote health awareness, not to provide a medical diagnosis.
                """
            )
            gr.Markdown("---")
            
            with gr.Accordion("🎯 Our Mission: The 'Why'", open=True):
                gr.Markdown(
                    """
                    We believe that awareness is the first and most powerful step towards a healthier life. 
                    This tool was built to help you:
                    *   **Gain Insight:** Understand how key health metrics can contribute to your overall risk profile.
                    *   **Encourage Proactive Care:** Use this information as a starting point for meaningful conversations with your doctor.
                    *   **Do It All Privately:** Your health data is sensitive. Our secure login ensures your prediction history is for your eyes only.
                    """
                )
            
            with gr.Accordion("🚀 Getting Started: The 'How'", open=False):
                gr.Markdown(
                    """
                    1.  **Create Your Secure Account:** Navigate to the **'Login / Signup'** tab. The process is quick and requires a username, email, password, and gender.
                    2.  **Enter Your Health Metrics:** Once logged in, go to the **'Prediction'** tab. Fill in the fields with your most recent health information.
                    3.  **Receive Your Instant Analysis:** Click the 'Predict My Risk' button. Our AI model will provide an immediate, educational assessment based on your data.
                    """
                )
            
            with gr.Accordion("⚠️ Important Disclaimer", open=False):
                gr.Markdown(
                    """
                    **This tool is NOT a substitute for professional medical advice, diagnosis, or treatment.**
                    The results from DiaSpark are for informational purposes only. Always seek the advice of your physician or another qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or seen on this application.
                    """
                )

        # --- Tab 2: Authentication ---
        with gr.TabItem("Login / Signup 🔑", id="auth_tab") as auth_tab_item:
            auth_message = gr.Markdown()
            
            with gr.Column(visible=True) as login_col:
                gr.Markdown("### Login to Your Account")
                email_login = gr.Textbox(label="Email", placeholder="Enter your email")
                pwd_login = gr.Textbox(label="Password", type="password", placeholder="Enter your password")
                login_btn = gr.Button("Login", variant="primary")
                show_signup_btn = gr.Button("New user? Sign up here.", variant="secondary")

            with gr.Column(visible=False) as signup_col:
                gr.Markdown("### Create a New Account")
                username_signup = gr.Textbox(label="Username", placeholder="Choose a unique username")
                email_signup = gr.Textbox(label="Email", placeholder="Enter your email")
                pwd_signup = gr.Textbox(
                    label="Password",
                    type="password",
                    placeholder="Create a password",
                    info="Must be at least 6 characters long."
                )
                gender_signup = gr.Radio(["Female", "Male"], label="Gender", info="This determines if the 'Pregnancies' field is shown.")
                signup_btn = gr.Button("Sign Up", variant="primary")
                show_login_btn = gr.Button("Already have an account? Login.", variant="secondary")
        
        # --- NEW "How to Use" Tab ---
        with gr.TabItem("How to Use 💡"):
            render_how_to_use_guide()

        # --- The rest of the informational and tool tabs ---
        with gr.TabItem("Learn About Diabetes 📚"):
            render_factors_info()
            
        with gr.TabItem("Healthy Eating Guide 🥗"):
            render_food_guide()
            
        with gr.TabItem("Find a Specialist 🧑‍⚕️"):
            render_doctor_list()

        # --- Prediction Tab ---
        with gr.TabItem("Prediction Tool 🔬", id="prediction_tab"):
            
            with gr.Column(visible=False) as prediction_view:
                gr.Markdown("### Enter Your Health Metrics for Prediction")
                gr.Markdown("---")
                
                with gr.Row(visible=False) as pregnancies_row:
                    preg = gr.Number(label="Pregnancies", info="Number of times pregnant")

                with gr.Row():
                    with gr.Column(scale=2):
                        glucose = gr.Number(label="Glucose", info="Plasma glucose concentration (mg/dL)")
                        bp = gr.Number(label="Blood Pressure", info="Diastolic (bottom number, mm Hg)")
                        insulin = gr.Number(label="Insulin", info="2-Hour serum insulin (mu U/ml)")
                        age = gr.Number(label="Age", info="Age in years")
                    
                    with gr.Column(scale=1):
                        bmi = gr.Number(label="BMI", info="Your Body Mass Index. We can calculate this for you.")
                        
                        bmi_choice = gr.Radio(
                            ["I know my BMI", "Calculate from Weight/Height"],
                            label="Provide BMI",
                            value="I know my BMI"
                        )
                        with gr.Column(visible=False) as bmi_calc_view:
                            weight = gr.Number(label="Your Weight (kg)")
                            height = gr.Number(label="Your Height (cm)")
                
                with gr.Row():
                    predict_btn = gr.Button("Predict My Risk", variant="primary")
                
                result_output = gr.Textbox(label="Prediction Result", interactive=False)
                
                generate_report_btn = gr.Button("Download Report as PDF", variant="secondary", visible=False)
                report_file_output = gr.File(label="Your Report", visible=False)
                
                logout_btn = gr.Button("Logout", variant="stop")

            with gr.Column(visible=True) as logged_out_view:
                gr.Markdown(
                    """
                    <div style="text-align:center; padding: 50px;">
                        <h2>🔒 Please log in to access the prediction tool.</h2>
                        <p>You can create an account or log in via the 'Login / Signup' tab.</p>
                    </div>
                    """
                )

    # --- Component Logic (Event Handlers) ---
    
    def switch_to_signup(): return gr.update(visible=False), gr.update(visible=True)
    def switch_to_login(): return gr.update(visible=True), gr.update(visible=False)
    show_signup_btn.click(fn=switch_to_signup, outputs=[login_col, signup_col])
    show_login_btn.click(fn=switch_to_login, outputs=[login_col, signup_col])
    
    def handle_user_state_change(user_data):
        is_logged_in = user_data.get("logged_in", False)
        is_female = user_data.get("gender") == "Female"
        username = user_data.get("username", "User")
        welcome_text = f"### 👋 Welcome, {username}!"
        return (gr.update(visible=is_logged_in), gr.update(visible=not is_logged_in), gr.update(visible=is_female), gr.update(value=welcome_text), gr.update(visible=is_logged_in), gr.update(visible=not is_logged_in))
    user_state.change(fn=handle_user_state_change, inputs=user_state, outputs=[prediction_view, logged_out_view, pregnancies_row, welcome_message, logged_in_header, auth_tab_item])

    signup_btn.click(fn=register, inputs=[email_signup, pwd_signup, gender_signup, username_signup], outputs=[auth_message, email_signup, pwd_signup, gender_signup, username_signup])
    login_btn.click(fn=login, inputs=[email_login, pwd_login, user_state], outputs=[auth_message, user_state, main_tabs])
    # The logout handler must now also clear the weight and height fields.
    logout_btn.click(fn=logout, inputs=[user_state], outputs=[auth_message, user_state, main_tabs, email_login, pwd_login, preg, glucose, bp, insulin, bmi, age, result_output, pregnancies_row, weight, height, bmi_choice])

    # --- BMI LOGIC ---
    def toggle_bmi_inputs(choice):
        if choice == "I know my BMI":
            # Return 4 values: one for each output component
            return gr.update(interactive=True, value=None), None, None, gr.update(visible=False)
        else: # Calculate from Weight/Height
            # Also return 4 values here to match the outputs list
            return gr.update(interactive=False, value=None), gr.update(), gr.update(), gr.update(visible=True)
    bmi_choice.change(fn=toggle_bmi_inputs, inputs=bmi_choice, outputs=[bmi, weight, height, bmi_calc_view])

    def calculate_bmi(w, h):
        if w and h and w > 0 and h > 0:
            bmi_val = round(w / ((h / 100) ** 2), 2)
            return bmi_val
        return None
    weight.change(fn=calculate_bmi, inputs=[weight, height], outputs=bmi)
    height.change(fn=calculate_bmi, inputs=[weight, height], outputs=bmi)

    predict_btn.click(fn=predict, inputs=[preg, glucose, bp, insulin, bmi, age, user_state], outputs=[result_output])
    
    def handle_create_report(user, p, g, b, i, bmi_val, age_val, result):
        if not result:
            return gr.update(visible=False)
        # Recalculate is no longer needed, just use the value from the bmi box
        final_bmi_report = bmi_val if bmi_val is not None else 0
        input_data = {"Pregnancies": p if p is not None else 0, "Glucose": g, "Blood Pressure": b, "Insulin": i, "BMI": final_bmi_report, "Age": age_val}
        file_path = create_report(user, input_data, result)
        # CORRECTED TYPO: It should be 'file_path', not 'file_file'
        return gr.update(value=file_path, visible=True)
    generate_report_btn.click(fn=handle_create_report, inputs=[user_state, preg, glucose, bp, insulin, bmi, age, result_output], outputs=[report_file_output])
    
    result_output.change(fn=lambda x: gr.update(visible=bool(x)), inputs=result_output, outputs=generate_report_btn)

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()

with gr.Blocks(title="DiaSpark: Your Health Management Platform", css=css) as demo:

    user_state = gr.State({"email": None, "id": None, "logged_in": False, "gender": None, "username": None})

    # --- Static Header (Always Visible) ---
    gr.Markdown("# 🩺 Welcome to DiaSpark: Your Health Management Platform")

    # --- Personalized Header (Visible only when logged in) ---
    with gr.Row(visible=False) as logged_in_header:
        welcome_message = gr.Markdown()

    # --- Main Tabs ---
    with gr.Tabs() as main_tabs:

        # --- Tab 1: Homepage ---
        with gr.TabItem("Home 🏠", id="home_tab"):
            gr.Markdown(
                "<h2 class='centered-text'>A Smart First Step in Understanding Your Health</h2>",
                elem_classes="centered-text"
            )
            gr.Markdown(
                """
                DiaSpark is a confidential tool that uses machine learning to provide an educational analysis of your diabetes risk factors.
                Our goal is to promote health awareness, not to provide a medical diagnosis.
                """
            )
            gr.Markdown("---")
            
            with gr.Accordion("🎯 Our Mission: The 'Why'", open=True):
                gr.Markdown(
                    """
                    We believe that awareness is the first and most powerful step towards a healthier life. 
                    This tool was built to help you:
                    *   **Gain Insight:** Understand how key health metrics can contribute to your overall risk profile.
                    *   **Encourage Proactive Care:** Use this information as a starting point for meaningful conversations with your doctor.
                    *   **Do It All Privately:** Your health data is sensitive. Our secure login ensures your prediction history is for your eyes only.
                    """
                )
            
            with gr.Accordion("🚀 Getting Started: The 'How'", open=False):
                gr.Markdown(
                    """
                    1.  **Create Your Secure Account:** Navigate to the **'Login / Signup'** tab. The process is quick and requires a username, email, password, and gender.
                    2.  **Enter Your Health Metrics:** Once logged in, go to the **'Prediction'** tab. Fill in the fields with your most recent health information.
                    3.  **Receive Your Instant Analysis:** Click the 'Predict My Risk' button. Our AI model will provide an immediate, educational assessment based on your data.
                    """
                )
            
            with gr.Accordion("⚠️ Important Disclaimer", open=False):
                gr.Markdown(
                    """
                    **This tool is NOT a substitute for professional medical advice, diagnosis, or treatment.**
                    The results from DiaSpark are for informational purposes only. Always seek the advice of your physician or another qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or seen on this application.
                    """
                )

        # --- Tab 2: Authentication ---
        with gr.TabItem("Login / Signup 🔑", id="auth_tab") as auth_tab_item:
            auth_message = gr.Markdown()
            
            with gr.Column(visible=True) as login_col:
                gr.Markdown("### Login to Your Account")
                email_login = gr.Textbox(label="Email", placeholder="Enter your email")
                pwd_login = gr.Textbox(label="Password", type="password", placeholder="Enter your password")
                login_btn = gr.Button("Login", variant="primary")
                show_signup_btn = gr.Button("New user? Sign up here.", variant="secondary")

            with gr.Column(visible=False) as signup_col:
                gr.Markdown("### Create a New Account")
                username_signup = gr.Textbox(label="Username", placeholder="Choose a unique username")
                email_signup = gr.Textbox(label="Email", placeholder="Enter your email")
                pwd_signup = gr.Textbox(
                    label="Password",
                    type="password",
                    placeholder="Create a password",
                    info="Must be at least 6 characters long."
                )
                gender_signup = gr.Radio(["Female", "Male"], label="Gender", info="This determines if the 'Pregnancies' field is shown.")
                signup_btn = gr.Button("Sign Up", variant="primary")
                show_login_btn = gr.Button("Already have an account? Login.", variant="secondary")
        
        # --- NEW "How to Use" Tab ---
        with gr.TabItem("How to Use 💡"):
            render_how_to_use_guide()

        # --- The rest of the informational and tool tabs ---
        with gr.TabItem("Learn About Diabetes 📚"):
            render_factors_info()
            
        with gr.TabItem("Healthy Eating Guide 🥗"):
            render_food_guide()
            
        with gr.TabItem("Find a Specialist 🧑‍⚕️"):
            render_doctor_list()

        # --- Prediction Tab ---
        with gr.TabItem("Prediction Tool 🔬", id="prediction_tab"):
            
            with gr.Column(visible=False) as prediction_view:
                gr.Markdown("### Enter Your Health Metrics for Prediction")
                gr.Markdown("---")
                
                with gr.Row(visible=False) as pregnancies_row:
                    preg = gr.Number(label="Pregnancies", info="Number of times pregnant")

                with gr.Row():
                    with gr.Column(scale=2):
                        glucose = gr.Number(label="Glucose", info="Plasma glucose concentration (mg/dL)")
                        bp = gr.Number(label="Blood Pressure", info="Diastolic (bottom number, mm Hg)")
                        insulin = gr.Number(label="Insulin", info="2-Hour serum insulin (mu U/ml)")
                        age = gr.Number(label="Age", info="Age in years")
                    
                    with gr.Column(scale=1):
                        bmi = gr.Number(label="BMI", info="Your Body Mass Index. We can calculate this for you.")
                        
                        bmi_choice = gr.Radio(
                            ["I know my BMI", "Calculate from Weight/Height"],
                            label="Provide BMI",
                            value="I know my BMI"
                        )
                        with gr.Column(visible=False) as bmi_calc_view:
                            weight = gr.Number(label="Your Weight (kg)")
                            height = gr.Number(label="Your Height (cm)")
                
                with gr.Row():
                    predict_btn = gr.Button("Predict My Risk", variant="primary")
                
                result_output = gr.Textbox(label="Prediction Result", interactive=False)
                
                generate_report_btn = gr.Button("Download Report as PDF", variant="secondary", visible=False)
                report_file_output = gr.File(label="Your Report", visible=False)
                
                logout_btn = gr.Button("Logout", variant="stop")

            with gr.Column(visible=True) as logged_out_view:
                gr.Markdown(
                    """
                    <div style="text-align:center; padding: 50px;">
                        <h2>🔒 Please log in to access the prediction tool.</h2>
                        <p>You can create an account or log in via the 'Login / Signup' tab.</p>
                    </div>
                    """
                )

    # --- Component Logic (Event Handlers) ---
    
    def switch_to_signup(): return gr.update(visible=False), gr.update(visible=True)
    def switch_to_login(): return gr.update(visible=True), gr.update(visible=False)
    show_signup_btn.click(fn=switch_to_signup, outputs=[login_col, signup_col])
    show_login_btn.click(fn=switch_to_login, outputs=[login_col, signup_col])
    
    def handle_user_state_change(user_data):
        is_logged_in = user_data.get("logged_in", False)
        is_female = user_data.get("gender") == "Female"
        username = user_data.get("username", "User")
        welcome_text = f"### 👋 Welcome, {username}!"
        return (gr.update(visible=is_logged_in), gr.update(visible=not is_logged_in), gr.update(visible=is_female), gr.update(value=welcome_text), gr.update(visible=is_logged_in), gr.update(visible=not is_logged_in))
    user_state.change(fn=handle_user_state_change, inputs=user_state, outputs=[prediction_view, logged_out_view, pregnancies_row, welcome_message, logged_in_header, auth_tab_item])

    signup_btn.click(fn=register, inputs=[email_signup, pwd_signup, gender_signup, username_signup], outputs=[auth_message, email_signup, pwd_signup, gender_signup, username_signup])
    login_btn.click(fn=login, inputs=[email_login, pwd_login, user_state], outputs=[auth_message, user_state, main_tabs])
    # The logout handler must now also clear the weight and height fields.
    logout_btn.click(fn=logout, inputs=[user_state], outputs=[auth_message, user_state, main_tabs, email_login, pwd_login, preg, glucose, bp, insulin, bmi, age, result_output, pregnancies_row, weight, height, bmi_choice])

    # --- BMI LOGIC ---
    def toggle_bmi_inputs(choice):
        if choice == "I know my BMI":
            # Return 4 values: one for each output component
            return gr.update(interactive=True, value=None), None, None, gr.update(visible=False)
        else: # Calculate from Weight/Height
            # Also return 4 values here to match the outputs list
            return gr.update(interactive=False, value=None), gr.update(), gr.update(), gr.update(visible=True)
    bmi_choice.change(fn=toggle_bmi_inputs, inputs=bmi_choice, outputs=[bmi, weight, height, bmi_calc_view])

    def calculate_bmi(w, h):
        if w and h and w > 0 and h > 0:
            bmi_val = round(w / ((h / 100) ** 2), 2)
            return bmi_val
        return None
    weight.change(fn=calculate_bmi, inputs=[weight, height], outputs=bmi)
    height.change(fn=calculate_bmi, inputs=[weight, height], outputs=bmi)

    predict_btn.click(fn=predict, inputs=[preg, glucose, bp, insulin, bmi, age, user_state], outputs=[result_output])
    
    def handle_create_report(user, p, g, b, i, bmi_val, age_val, result):
        if not result:
            return gr.update(visible=False)
        # Recalculate is no longer needed, just use the value from the bmi box
        final_bmi_report = bmi_val if bmi_val is not None else 0
        input_data = {"Pregnancies": p if p is not None else 0, "Glucose": g, "Blood Pressure": b, "Insulin": i, "BMI": final_bmi_report, "Age": age_val}
        file_path = create_report(user, input_data, result)
        # CORRECTED TYPO: It should be 'file_path', not 'file_file'
        return gr.update(value=file_path, visible=True)
    generate_report_btn.click(fn=handle_create_report, inputs=[user_state, preg, glucose, bp, insulin, bmi, age, result_output], outputs=[report_file_output])
    
    result_output.change(fn=lambda x: gr.update(visible=bool(x)), inputs=result_output, outputs=generate_report_btn)

# --- Launch the App ---
if __name__ == "__main__":
    demo.launch()
