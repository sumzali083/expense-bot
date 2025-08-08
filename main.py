# main.py
from dotenv import load_dotenv
load_dotenv()  # safe to keep even if reporter also loads

from email_fetcher import fetch_attachments
from parser import parse_csv, parse_pdf
from matcher import flag_anomalies
from reporter import send_slack_report
import glob, pandas as pd, os

def main():
    # DEBUG: confirm what token main sees
    print("DEBUG token starts with:", (os.getenv("SLACK_TOKEN") or "")[:5])
    fetch_attachments()
    dfs = []
    for file in glob.glob("attachments/*"):
        if file.endswith(".csv"):
            dfs.append(parse_csv(file))
        elif file.endswith(".pdf"):
            dfs.append(parse_pdf(file))
    combined = pd.concat(dfs, ignore_index=True)
    anomalies = flag_anomalies(combined)
    send_slack_report(anomalies)

if __name__=="__main__":
    main()
