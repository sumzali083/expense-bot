# reporter.py

from slack_sdk import WebClient
import os

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
CHANNEL     = "#expenses"  # adjust to your Slack channel or user ID

def send_slack_report(df):
    client = WebClient(token=SLACK_TOKEN)
    if df.empty:
        text = "✅ All expenses are within policy."
    else:
        lines = df.apply(
            lambda r: f"{r.Date} • {r.Merchant} • £{r.Amount:.2f} • {r.Category}",
            axis=1
        )
        text = "⚠️ *Policy anomalies detected:*\n" + "\n".join(lines)
    client.chat_postMessage(channel=CHANNEL, text=text)
