import pandas as pd
import pdfplumber

def parse_csv(path):
    return pd.read_csv(path)

def parse_pdf(path):
    rows = []
    with pdfplumber.open(path) as pdf:
        text = "\n".join(p.extract_text() for p in pdf.pages)
    for line in text.split("\n"):
        parts = [p.strip() for p in line.split("|")]
        if len(parts)==4:
            rows.append({
                "Date": parts[0],
                "Merchant": parts[1],
                "Amount": float(parts[2].lstrip("£")),
                "Category": parts[3]
            })
    return pd.DataFrame(rows)
