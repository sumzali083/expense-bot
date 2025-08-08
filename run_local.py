# run_local.py
import os, glob, pandas as pd

# Minimal policy
POLICY = {
    "Travel": {"max_amount": 50.0},
    "Meals":  {"max_amount": 25.0},
}

EXPECTED = {"Date","Merchant","Amount","Category"}

def flag_anomalies(df):
    df = df.copy()
    df["Allowed"] = df.apply(
        lambda r: r["Amount"] <= POLICY.get(r["Category"], {}).get("max_amount", 0),
        axis=1
    )
    return df[~df["Allowed"]]

def main():
    os.makedirs("out", exist_ok=True)
    dfs = []
    for path in glob.glob("attachments/*.csv"):
        d = pd.read_csv(path)
        if EXPECTED.issubset(set(d.columns)):
            dfs.append(d[["Date","Merchant","Amount","Category"]])
        else:
            print(f"Skipping {path} (wrong columns: {list(d.columns)})")

    if not dfs:
        print("No valid CSVs in attachments/. Put a sample there and re-run.")
        return

    all_expenses = pd.concat(dfs, ignore_index=True)
    anomalies = flag_anomalies(all_expenses)

    # Save outputs
    all_expenses.to_csv("out/all_expenses.csv", index=False)
    anomalies.to_csv("out/anomalies.csv", index=False)

    # Tiny HTML report for screenshots
    summary = f"""
    <h2>Expense Bot – Local Report</h2>
    <p>Total rows: {len(all_expenses)} | Anomalies: {len(anomalies)}</p>
    <h3>Anomalies</h3>
    {anomalies.to_html(index=False)}
    """
    with open("out/report.html", "w", encoding="utf-8") as f:
        f.write(summary)

    print("✅ Wrote out/all_expenses.csv, out/anomalies.csv, out/report.html")

if __name__ == "__main__":
    main()
