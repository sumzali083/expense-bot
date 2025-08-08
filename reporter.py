# reporter.py
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

def send_slack_report(df, channel=None):
    load_dotenv()  # load .env now
    token = os.getenv("SLACK_TOKEN", "").strip()
    channel = channel or os.getenv("SLACK_CHANNEL", "").strip() or "#general"

    if not token.startswith("xoxb-"):
        raise RuntimeError("SLACK_TOKEN missing/invalid. Must be a bot token starting with 'xoxb-'.")

    client = WebClient(token=token)
    if df.empty:
        text = "✅ All expenses are within policy."
    else:
        lines = df.apply(lambda r: f"{r.Date} • {r.Merchant} • £{float(r.Amount):.2f} • {r.Category}", axis=1)
        text = "⚠️ *Policy anomalies detected:*\n" + "\n".join(lines)
    client.chat_postMessage(channel=channel, text=text)


