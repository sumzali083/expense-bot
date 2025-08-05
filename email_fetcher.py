from dotenv import load_dotenv
load_dotenv()
import os



import os, imaplib, email
from email.header import decode_header

IMAP_HOST = os.getenv("EMAIL_HOST")
USER = os.getenv("EMAIL_USER")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def fetch_attachments(save_dir="attachments"):
    os.makedirs(save_dir, exist_ok=True)
    mail = imaplib.IMAP4_SSL(IMAP_HOST)
    mail.login(USER, PASSWORD)
    mail.select("inbox")
    _, nums = mail.search(None, "UNSEEN")
    for n in nums[0].split():
        _, data = mail.fetch(n, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        for part in msg.walk():
            if part.get_content_maintype()=="multipart": continue
            filename = part.get_filename()
            if filename:
                path = os.path.join(save_dir, decode_header(filename)[0][0])
                with open(path, "wb") as f:
                    f.write(part.get_payload(decode=True))
                print(f"Saved {path}")
    mail.logout()

if __name__=="__main__":
    fetch_attachments()
