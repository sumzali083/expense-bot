# test_slack.py
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

load_dotenv()
token = os.getenv("SLACK_TOKEN", "")
channel = os.getenv("SLACK_CHANNEL", "")

print("Token starts with:", token[:5])  # should print 'xoxb-'
client = WebClient(token=token)
print(client.auth_test())               # should return ok=True
client.chat_postMessage(channel=channel, text="Hello from ExpenseBot test ✅")
print("Posted.")
