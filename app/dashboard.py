import os
import plotly.express as px
from prophet import Prophet
from email_alert import send_email_alert
from anomaly_detector import detect_anomalies
import streamlit as st
import matplotlib.pyplot as plt
from cost_predictor import load_data, predict_cost
from optimizer import suggest_optimizations
import pandas as pd

st.sidebar.header("📧 Email Alert Tester")

# Input fields for test email configuration
recipient_email = st.sidebar.text_input("Recipient Email", "your_email@gmail.com")
sender_email = st.sidebar.text_input("Sender Gmail", "your_gmail@gmail.com")
sender_password = st.sidebar.text_input("Gmail App Password", type="password")

if st.sidebar.button("Send Test Email"):
    try:
        send_email_alert(
            subject="✅ AI Cost Optimizer Test Email",
            body="This is a test email from your AI Cost Optimizer project.",
            recipient_email=recipient_email,
            sender_email=sender_email,
            sender_password=sender_password
        )
        st.sidebar.success("✅ Test email sent successfully!")
    except Exception as e:
        st.sidebar.error(f"❌ Failed to send email: {e}")


st.title("💡 AI-Powered Cloud Cost Predictor & Optimizer")

# 1️⃣ Load both original & daily cost data
raw_df = pd.read_csv("data/aws_billing_mock.csv")   # Original with Service column
df = load_data("data/aws_billing_mock.csv")         # Aggregated for Prophet

# 2️⃣ Run prediction
forecast = predict_cost(df)

# 3️⃣ Get optimization suggestions using full dataset
suggestions = suggest_optimizations(raw_df)

# 4️⃣ Show cost data
st.subheader("📊 Historical Cost Data")
st.line_chart(df.set_index('ds')['y'])

# 5️⃣ Show prediction
st.subheader("🔮 Predicted Future Cost (Next 30 Days)")
fig, ax = plt.subplots()
ax.plot(forecast['ds'], forecast['yhat'], label='Predicted')
ax.set_xlabel("Date")
ax.set_ylabel("Predicted Cost (₹)")
st.pyplot(fig)

# 6️⃣ Show AI optimization tips
st.subheader("🧠 AI Optimization Suggestions")
for s in suggestions:
    st.write("-", s)
# 7️⃣ Detect anomalies
st.subheader("🚨 Anomaly Detection (Cost Spikes)")
anomalies, alerts = detect_anomalies(df)

if len(alerts) > 0:
    for alert in alerts:
        st.error(alert)
else:
    st.success("✅ No anomalies detected. Spending is stable.")

# Plot anomalies
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(df['ds'], df['y'], label='Cost')
ax.scatter(anomalies['ds'], anomalies['y'], color='red', label='Anomalies', marker='o')
ax.set_xlabel("Date")
ax.set_ylabel("Cost (₹)")
ax.legend()
st.pyplot(fig)
# 8️⃣ Send email if anomalies detected
if len(alerts) > 0:
    subject = "⚠️ AI Cost Optimizer Alert: Cost Spike Detected"
    body = "\n".join(alerts)
    recipient_email = "your_email@gmail.com"  # change this
    sender_email = "your_gmail@gmail.com"     # change this
    sender_password = "your_app_password_here"

    send_email_alert(subject, body, recipient_email, sender_email, sender_password)
    st.warning("📧 Email alert sent!")

    # 9️⃣ AWS Live Cost Tracker
st.header("☁️ AWS Cost Tracker")

if os.path.exists("aws_cost_data.csv"):
    df_aws = pd.read_csv("aws_cost_data.csv")
    df_aws['ds'] = pd.to_datetime(df_aws['ds'])
    st.success("✅ AWS Cost Data Loaded")

    # Plot daily AWS cost trend
    fig1 = px.line(df_aws, x='ds', y='y', title="Daily AWS Cost (Last 30 Days)")
    st.plotly_chart(fig1, use_container_width=True)

    # AI Forecast for next 7 days
    st.subheader("🤖 7-Day AI Forecast")
    model = Prophet()
    model.fit(df_aws.rename(columns={"ds": "ds", "y": "y"}))
    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)
    fig2 = px.line(forecast, x="ds", y="yhat", title="Forecasted AWS Cost (Next 7 Days)")
    st.plotly_chart(fig2, use_container_width=True)

    # Detect anomalies
    df_aws['z_score'] = (df_aws['y'] - df_aws['y'].mean()) / df_aws['y'].std()
    anomalies = df_aws[df_aws['z_score'].abs() > 2]
    if not anomalies.empty:
        st.warning("⚠️ Anomalies Detected in AWS Spend:")
        st.dataframe(anomalies[['ds', 'y', 'z_score']])
    else:
        st.info("✅ No AWS cost anomalies detected.")
else:
    st.error("❌ No AWS cost data found. Run `python3 fetch_aws_cost.py` first.")

