import streamlit as st
import os
from modules.extract import extract_tables_from_pdf
from modules.parser import parse_risk_scenario_tables
from modules.exporter import export_to_excel

st.title("📄 Risk Scenario PDF → Excel Converter")
st.write("Upload one or multiple PDF files to extract Risk Scenario tables automatically.")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

output_dir = "output"

if uploaded_files:
    st.info(f"Processing {len(uploaded_files)} files...")

    for pdf in uploaded_files:
        with st.spinner(f"Extracting data from: {pdf.name}"):

            # Extract all tables
            tables = extract_tables_from_pdf(pdf)

            # Parse only risk scenario rows
            parsed_rows = parse_risk_scenario_tables(tables)

            if not parsed_rows:
                st.warning(f"No risk scenario table found in {pdf.name}")
                continue

            # Export to Excel
            output_path = os.path.join(
                output_dir,
                pdf.name.replace(".pdf", "_Risk_Scenarios.xlsx")
            )

            export_to_excel(parsed_rows, output_path)

            st.success(f"Extracted & saved: {output_path}")

            # Download button
            with open(output_path, "rb") as f:
                st.download_button(
                    label=f"Download Excel for {pdf.name}",
                    data=f,
                    file_name=os.path.basename(output_path),
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    st.success("All files processed successfully! 🎉")
``
