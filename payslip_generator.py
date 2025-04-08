import os
import pandas as pd
from fpdf import FPDF
import yagmail
from dotenv import load_dotenv

# Load email config from .env
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Create output folder
os.makedirs("payslips", exist_ok=True)

# Read Excel file
df = pd.read_excel("employees.xlsx")

# Generate Payslip PDF
def generate_payslip(emp_id, name, basic, allow, deduct, net_salary):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Payslip", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(100, 10, txt=f"Employee ID: {emp_id}", ln=True)
    pdf.cell(100, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(100, 10, txt=f"Basic Salary: ${basic:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Allowances: ${allow:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Deductions: ${deduct:.2f}", ln=True)
    pdf.cell(100, 10, txt=f"Net Salary: ${net_salary:.2f}", ln=True)

    filename = f"payslips/{emp_id}.pdf"
    pdf.output(filename)
    return filename

# Send Email
def send_email(to_email, pdf_file, name):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, EMAIL_PASSWORD)
        yag.send(
            to=to_email,
            subject="Your Payslip for This Month",
            contents=f"Hi {name},\n\nPlease find attached your payslip for this month.\n\nBest regards,\nHR Team",
            attachments=pdf_file,
        )
        print(f"Email sent to {name} ({to_email})")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Process Each Employee
for index, row in df.iterrows():
    emp_id = row["Employee ID"]
    name = row["Name"]
    email = row["Email"]
    basic = float(row["Basic Salary"])
    allow = float(row["Allowances"])
    deduct = float(row["Deductions"])
    net_salary = basic + allow - deduct

    pdf_path = generate_payslip(emp_id, name, basic, allow, deduct, net_salary)
    send_email(email, pdf_path, name)
