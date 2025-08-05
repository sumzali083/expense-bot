# test_matcher.py
import pandas as pd
from matcher import flag_anomalies

# Build a DataFrame with one exceeding row
df = pd.DataFrame([
    {"Date":"2025-07-30","Merchant":"ACME","Amount":60,"Category":"Travel"},
    {"Date":"2025-07-29","Merchant":"Cafe","Amount":20,"Category":"Meals"}
])

print("All rows:\n", df, "\n")
print("Anomalies flagged:\n", flag_anomalies(df))
