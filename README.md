# 🧾 Payslip Generator with Email Automation

This Python script reads employee details from an Excel file, calculates net salaries, generates individual PDF payslips, and sends them to employees via email.

## 📂 Project Structure

```
Payslip_project/
│
├── employees.xlsx            # Sample Excel file with employee data
├── payslip_generator.py      # Main script to generate and send payslips
├── payslips/                 # Folder where generated PDFs will be stored
├── .env                      # Environment variables for email credentials (you create this)
└── README.md                 # This file
```



| Employee ID | Name       | Email               | Basic Salary | Allowances | Deductions |
|-------------|------------|---------------------|---------------|-------------|-------------|
| 001         | Alice Doe  | alice@example.com   | 5000          | 300         | 200         |
| 002         | Bob Smith  | bob@example.com     | 6000          | 400         | 300         |

## ⚙️ How It Works

1. Reads employee data from `employees.xlsx`.
2. Calculates Net Salary = Basic Salary + Allowances - Deductions.
3. Generates a PDF payslip for each employee in the `payslips/` folder.
4. Sends the PDF as an email attachment to each employee.




## ▶️ How to Run the Script

```bash
python payslip_generator.py
```

The script will:
- Generate payslips and save them as PDFs in the `payslips/` folder.
- Email each PDF to the respective employee's email address.

## ✅ Output Example

- Payslip PDFs saved in:
  ```
  payslips/001.pdf
  payslips/002.pdf
  ...
  ```

## 🛡 Error Handling

- If the script fails to send an email (e.g., wrong credentials), it will print an error message but continue running for other employees.
