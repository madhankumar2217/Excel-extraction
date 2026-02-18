from docx import Document

def extract_tables_from_docx(file):
    doc = Document(file)
    extracted_tables = []

    for table in doc.tables:
        rows = []
        for row in table.rows:
            cells = [cell.text.strip() for cell in row.cells]
            rows.append(cells)
        extracted_tables.append(rows)

    return extracted_tables
