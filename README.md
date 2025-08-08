# Expense Bot
Python tool that parses expense CSVs, checks simple policy rules (e.g., Travel ≤ £50, Meals ≤ £25), and outputs an HTML/CSV report of anomalies.

## Run
python -m venv venv && venv\Scripts\activate.bat
pip install -r requirements.txt
mkdir attachments
# put a CSV with: Date,Merchant,Amount,Category
python run_local.py  # generates out/report.html
