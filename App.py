import pdfplumber
import pandas as pd
import os
import re

input_folder = "RiskPDFs"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

def extract_risk_table(pdf_path):
    rows = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                # Filter rows that contain numerical Ref No (1–9+)
                for row in table:
                    if row and re.match(r"^\s*\d+\s*$", str(row[1])):
                        ref_no = int(row[1])
                        section = row[2]
                        scenario = row[3]
                        harmful_effect = row[4]
                        severity_before = row[5]
                        prob_before = row[6]
                        protective = row[7]
                        severity_after = row[8]
                        prob_after = row[9]

                        rows.append([
                            ref_no, section, scenario, harmful_effect,
                            severity_before, prob_before,
                            protective, severity_after, prob_after
                        ])
    return rows

for file in os.listdir(input_folder):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, file)
        data = extract_risk_table(pdf_path)

        df = pd.DataFrame(data, columns=[
            "Ref No", "Section / Point", "Scenario",
            "Harmful Event / Effect", "Severity (Before)",
            "Probability (Before)", "Protective Measures",
            "Severity (After)", "Probability (After)"
        ])

        out_file = os.path.join(
            output_folder,
            file.replace(".pdf", "_Risk_Scenarios.xlsx")
        )
        df.to_excel(out_file, index=False, engine="openpyxl")

        print("Created:", out_file)
