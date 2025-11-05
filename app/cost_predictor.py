import pandas as pd
from prophet import Prophet

def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    daily_cost = df.groupby('Date')['Cost'].sum().reset_index()
    daily_cost.columns = ['ds', 'y']
    return daily_cost

def predict_cost(df):
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast
