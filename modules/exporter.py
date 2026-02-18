import pandas as pd
import os

def export_to_excel(rows, output_path):
    df = pd.DataFrame(rows)

    # Ensure folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_excel(output_path, index=False, engine="openpyxl")
    return output_path
