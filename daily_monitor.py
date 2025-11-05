import pandas as pd
from app.anomaly_detector import detect_anomalies
from app.email_alert import send_email_alert
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Example cost data (replace with your real billing CSV path)
data_path = "data/aws_billing_mock.csv"

def run_daily_monitor():
    print("🚀 Running daily AI cost monitor...")

    # Load dataset
    df = pd.read_csv(data_path)

    # Rename columns to match expected format
    df['ds'] = pd.to_datetime(df['Date'])
    df['y'] = df['Cost'].astype(float)

    # Optional: group by date in case multiple services exist
    df_daily = df.groupby('ds')['y'].sum().reset_index()

    print("✅ Loaded cost data:")
    print(df_daily.head())

    # Detect anomalies
    anomalies = detect_anomalies(df_daily)

    if not anomalies.empty:
        print("⚠️ Anomalies detected:")
        print(anomalies)

        # Send email alert
        send_email_alert(
            subject="⚠️ AWS Cost Anomaly Detected",
            body=f"Anomaly detected in your AWS billing data:\n\n{anomalies.to_string(index=False)}",
            recipient_email=os.getenv("ALERT_EMAIL"),
            sender_email=os.getenv("SENDER_EMAIL"),
            sender_password=os.getenv("SENDER_PASSWORD")
        )
    else:
        print("✅ No anomalies detected today.")

if __name__ == "__main__":
    run_daily_monitor()
