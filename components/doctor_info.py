# components/doctor_info.py

import gradio as gr

def render_doctor_list():
    """
    Creates and returns the Gradio UI for the 'Consult a Specialist' section,
    now with contact numbers and clickable website links.
    """
    with gr.Blocks() as doctors_ui:
        gr.Markdown("## 👨‍⚕️ Consult a Specialist in India")
        
        # --- Strengthened Disclaimer ---
        gr.Markdown(
            """
            > **⚠️ IMPORTANT DISCLAIMER:**
            > This list is for informational purposes ONLY and is not a direct endorsement or recommendation. 
            > The information provided is based on publicly available data and is subject to change. 
            > **You must conduct your own research and verify all contact information directly with the hospital or clinic before making an appointment.**
            > DiaSpark is not responsible for the accuracy of this third-party information.
            """
        )
        gr.Markdown("---")

        with gr.Accordion("Dr. V. Mohan - Chennai", open=True):
            gr.Markdown(
                """
                *   **🩺 Specialization:** Diabetologist
                *   **🏥 Clinic/Hospital:** Dr. Mohan's Diabetes Specialities Centre
                *   **📍 City:** Chennai
                *   **💡 Notable For:** A world-renowned researcher and clinician, recipient of the Padma Shri. His centre is a WHO Collaborating Centre.
                *   **📞 Contact Info:** +91-44-4396-8888 (General Line - Please Verify)
                *   **🌐 Website:** [Dr. Mohan's Diabetes Specialities Centre](https://drmohans.com/)
                """
            )

        with gr.Accordion("Dr. Ambrish Mithal - Delhi NCR", open=False):
            gr.Markdown(
                """
                *   **🩺 Specialization:** Endocrinology & Diabetes
                *   **🏥 Clinic/Hospital:** Max Healthcare (Yashoda Super Speciality Hospital)
                *   **📍 City:** Delhi / Gurugram
                *   **💡 Notable For:** A highly awarded endocrinologist, recipient of the Padma Bhushan, with extensive experience in complex diabetic disorders.
                *   **📞 Contact Info:** +91-11-4055-4055 (Max Healthcare Helpline - Please Verify)
                *   **🌐 Website:** [Max Healthcare Official Site](https://www.maxhealthcare.in/)
                """
            )

        with gr.Accordion("Dr. V. S. Sheshiah - Chennai", open=False):
            gr.Markdown(
                """
                *   **🩺 Specialization:** Diabetologist
                *   **🏥 Clinic/Hospital:** Apollo Hospitals, Greams Road
                *   **📍 City:** Chennai
                *   **💡 Notable For:** A pioneer in diabetes care in India, especially renowned for his work on gestational diabetes.
                *   **📞 Contact Info:** +91-44-2829-3333 (Apollo Chennai General Line - Please Verify)
                *   **🌐 Website:** [Apollo Hospitals, Chennai](https://chennai.apollohospitals.com/)
                """
            )
        
        with gr.Accordion("Dr. Anoop Misra - New Delhi", open=False):
            gr.Markdown(
                """
                *   **🩺 Specialization:** Internal Medicine & Diabetes
                *   **🏥 Clinic/Hospital:** Fortis C-DOC Hospital for Diabetes
                *   **📍 City:** New Delhi
                *   **💡 Notable For:** Another Padma Shri awardee, known for extensive research on diabetes in the South Asian population. He is the Chairman at Fortis C-DOC.
                *   **📞 Contact Info:** +91-11-4910-1222 (Fortis C-DOC Appointment Line - Please Verify)
                *   **🌐 Website:** [Fortis C-DOC Website](https://www.fortiscdoc.com/)
                """
            )