# matcher.py

# Define your allowed maximums per category
POLICY = {
    "Travel": {"max_amount": 50.0},
    "Meals":  {"max_amount": 25.0},
}

def flag_anomalies(df):
    """Return only rows where Amount exceeds the POLICY limit."""
    df["Allowed"] = df.apply(
        lambda r: r["Amount"] <= POLICY.get(r["Category"], {}).get("max_amount", 0),
        axis=1
    )
    return df[~df["Allowed"]]
