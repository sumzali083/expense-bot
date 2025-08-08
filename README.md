# Expense Bot
Python tool that parses expense CSVs, checks simple policy rules (e.g., Travel ≤ £50, Meals ≤ £25), and outputs an HTML/CSV report of anomalies.

## Run
python -m venv venv && venv\Scripts\activate.bat
pip install -r requirements.txt
mkdir attachments
# put a CSV with: Date,Merchant,Amount,Category
python run_local.py  # generates out/report.html

<img width="1347" height="565" alt="Image" src="https://github.com/user-attachments/assets/cb7bc408-8caf-4ec1-a253-dc4ecd214265" />
