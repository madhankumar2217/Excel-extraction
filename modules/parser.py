import re

def parse_risk_scenario_tables(tables):
    parsed_rows = []

    for table in tables:
        for row in table:
            if len(row) < 10:
                continue

            # Check if the second column is a Ref No (1–200 etc.)
            if row[1] and re.match(r"^\d+$", str(row[1]).strip()):
                parsed_rows.append({
                    "Ref No": row[1],
                    "Section / Point": row[2],
                    "Scenario": row[3],
                    "Harmful Event / Effect": row[4],
                    "Severity (Before)": row[5],
                    "Probability (Before)": row[6],
                    "Protective Measures": row[7],
                    "Severity (After)": row[8],
                    "Probability (After)": row[9],
                })

    return parsed_rows
