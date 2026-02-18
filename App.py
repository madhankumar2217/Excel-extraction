import streamlit as st
from modules.docx_reader import extract_tables_from_docx
from modules.excel_exporter import tables_to_excel
import os

st.title("📄 Word Table → Excel Extractor")
st.write("Upload multiple DOCX files and extract all tables into Excel automatically.")

uploaded_files = st.file_uploader(
    "Upload Word files (.docx)",
    type=["docx"],
    accept_multiple_files=True
)

OUTPUT_DIR = "output"

if uploaded_files:
    st.info(f"Processing {len(uploaded_files)} Word files...")

    for file in uploaded_files:
        with st.spinner(f"Extracting tables from {file.name}..."):

            try:
                tables = extract_tables_from_docx(file)
            except Exception as e:
                st.error(f"Error reading {file.name}: {e}")
                continue

            if not tables:
                st.warning(f"No tables found in {file.name}")
                continue

            output_path = os.path.join(
                OUTPUT_DIR,
                file.name.replace(".docx", "_tables.xlsx")
            )

            tables_to_excel(tables, output_path)

            st.success(f"Extracted: {output_path}")

            with open(output_path, "rb") as f:
                st.download_button(
                    label=f"⬇️ Download Excel for {file.name}",
                    data=f,
                    file_name=os.path.basename(output_path),
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    st.success("🎉 All files processed successfully!")
