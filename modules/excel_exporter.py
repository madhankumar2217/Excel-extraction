import pandas as pd
import os

def tables_to_excel(tables, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    writer = pd.ExcelWriter(output_path, engine="openpyxl")

    for i, table in enumerate(tables):
        df = pd.DataFrame(table)
        df.to_excel(writer, sheet_name=f"Table_{i+1}", index=False)

    writer.save()
    return output_path
