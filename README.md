# 🩺 DiaSpark: AI-Powered Diabetes Health Platform

DiaSpark is a comprehensive web application built with Gradio and Python, designed to help users assess their risk of diabetes and manage their health proactively. The app provides an AI-based prediction, informational resources, and tools for personal health logging.

---

## ✅ Features

- **AI-Powered Prediction:** Uses a machine learning model to predict diabetes risk based on key health metrics.
- **Secure User Accounts:** Full authentication system powered by Supabase for user registration and login.
- **Dynamic UI:** The interface intelligently adapts based on user input (e.g., showing a "Pregnancies" field only for female users).
- **Automated BMI Calculator:** Users can either enter their BMI directly or have it calculated instantly from their weight and height.
- **Downloadable PDF Reports:** Users can download a well-structured PDF summary of their prediction results, complete with a logo and disclaimer.
- **Rich Informational Content:** Includes dedicated, easy-to-read sections on:
  - Factors Affecting Diabetes
  - A Healthy Eating Guide
  - A list of Specialist Doctors in India
  - A "How to Use" guide for the prediction tool
- **State-of-the-Art UI:** The interface is built to be intuitive, hiding irrelevant tabs or fields to reduce clutter and guide the user experience.

---

## 🛠️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/DiaSpark-Diabetes-App.git
    cd DiaSpark-Diabetes-App
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    This project requires a connection to a Supabase backend. You will need to create a `.env` file in the root directory and add your Supabase credentials:
    ```
    SUPABASE_URL="https://YOUR_SUPABASE_URL.supabase.co"
    SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"
    ```
    *The `utils/db.py` file is configured to read these variables. You may need to install `python-dotenv` (`pip install python-dotenv`) and add code to load the .env file if running locally.*

5.  **Run the application:**
    ```bash
    python app.py
    ```

---

## ⚙️ Supabase Configuration

The backend relies on a specific Supabase project setup:

1.  **Tables:** Two main tables are required (`users` and `predictions`). You can find their schemas in the SQL files or by examining the code.
2.  **Database Triggers:** An essential trigger is used to automatically create a public `users` profile every time a new user signs up in the `auth.users` table. This trigger must be set up in the Supabase SQL Editor for the signup process to work.
