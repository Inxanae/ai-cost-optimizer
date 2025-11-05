import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def send_email_alert(subject, body, recipient_email, sender_email=None, sender_password=None):
    """
    Sends an email alert with the given subject and body.
    If sender_email or sender_password not provided, it reads from .env file.
    """

    # Load from environment if not passed
    if sender_email is None:
        sender_email = os.getenv("SENDER_EMAIL")
    if sender_password is None:
        sender_password = os.getenv("SENDER_PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {recipient_email}")
    except Exception as e:
        print(f"❌ Email failed: {e}")
