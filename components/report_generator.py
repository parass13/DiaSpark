from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        # Logo
        # The 'logo.png' file must exist in the root directory of your project
        try:
            self.image('logo.png', 10, 8, 33)
        except FileNotFoundError:
            self.set_font('Helvetica', 'B', 12)
            self.cell(0, 10, 'DiaSpark Logo Not Found', 0, 1, 'L')
        # App Title
        self.set_font('Helvetica', 'B', 20)
        self.cell(0, 10, 'DiaSpark Health Report', 0, 1, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Helvetica italic 8
        self.set_font('Helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_report(user_data, input_data, prediction_result):
    """
    Generates a PDF report from user data and returns the file path.
    """
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Helvetica', '', 12)
    
    # --- Report Header ---
    pdf.set_font('Helvetica', 'B', 16)
    pdf.cell(0, 10, 'Confidential Health Prediction Summary', 0, 1, 'L')
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(0, 8, f"Report for: {user_data.get('username', 'N/A')}", 0, 1, 'L')
    pdf.cell(0, 8, f"Date Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'L')
    pdf.ln(10)

    # --- Input Data Table ---
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 10, 'Submitted Health Metrics', 0, 1, 'L')
    
    # Table Header
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_fill_color(230, 230, 230) # Light grey background
    pdf.cell(95, 10, 'Metric', 1, 0, 'C', fill=True)
    pdf.cell(95, 10, 'Value', 1, 1, 'C', fill=True)

    # Table Rows
    pdf.set_font('Helvetica', '', 11)
    for key, value in input_data.items():
        pdf.cell(95, 10, key, 1, 0, 'L')
        pdf.cell(95, 10, str(value), 1, 1, 'L')
    pdf.ln(10)

    # --- Prediction Result ---
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 10, 'Prediction Result', 0, 1, 'L')
    
    is_diabetic = "Diabetic" in prediction_result
    result_text = prediction_result.replace("✅ ", "").replace("🟢 ", "") # Clean up emojis
    
    # Set color based on result
    if is_diabetic:
        pdf.set_text_color(194, 8, 8) # Red
    else:
        pdf.set_text_color(34, 139, 34) # Green
        
    pdf.set_font('Helvetica', 'B', 18)
    pdf.cell(0, 15, result_text, 1, 1, 'C')
    pdf.set_text_color(0, 0, 0) # Reset to black
    pdf.ln(10)

    # --- Disclaimer ---
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 10, 'IMPORTANT DISCLAIMER', 0, 1, 'L')
    pdf.set_font('Helvetica', 'I', 10)
    pdf.multi_cell(0, 5, 
        "This report is generated by an AI model and is for informational purposes ONLY. "
        "It is NOT a medical diagnosis. Please consult with a qualified healthcare professional "
        "for any health concerns or before making any decisions related to your health. "
        "DiaSpark is not responsible for any actions taken based on this report."
    )
    
    # --- Save the PDF ---
    file_path = "diaspark_report.pdf"
    pdf.output(file_path)
    return file_path