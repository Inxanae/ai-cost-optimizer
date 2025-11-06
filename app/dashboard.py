import streamlit as st
import pandas as pd
import boto3
from datetime import datetime
from prophet import Prophet

st.set_page_config(page_title="AI Cost Optimizer", layout="wide")

# Title
st.title("Predictive AWS Cost Optimization Dashboard")

# --- CACHE AWS COST DATA ---
@st.cache_data(ttl=86400)  # Cache for 24 hours
def get_aws_cost_data():
    client = boto3.client('ce', region_name='us-east-1')
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': '2024-10-01',
            'End': datetime.now().strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    
    # Parse AWS data
    df = pd.DataFrame([
        {
            "Date": item['TimePeriod']['Start'],
            "Cost": float(item['Metrics']['UnblendedCost']['Amount'])
        }
        for item in response['ResultsByTime']
    ])
    return df

# --- FETCH DATA ---
data = get_aws_cost_data()

# --- DISPLAY CURRENT COSTS ---
st.subheader("AWS Daily Cost Trend")
st.line_chart(data.set_index("Date")["Cost"])

# --- FORECAST FUTURE COSTS (AI PART) ---
st.subheader("Predicted AWS Monthly Cost")
df = data.rename(columns={"Date": "ds", "Cost": "y"})

model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

st.line_chart(forecast.set_index("ds")[["yhat", "yhat_lower", "yhat_upper"]])

# --- INFO ---
st.caption(f"Data last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.success("✅ Data auto-refreshes every 24 hours.")
