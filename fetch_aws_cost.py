import boto3
import pandas as pd
from datetime import datetime, timedelta

def get_daily_cost():
    ce = boto3.client('ce')
    end = datetime.utcnow().date()
    start = end - timedelta(days=30)

    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start.strftime('%Y-%m-%d'), 'End': end.strftime('%Y-%m-%d')},
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    data = []
    for result in response['ResultsByTime']:
        date = result['TimePeriod']['Start']
        amount = float(result['Total']['UnblendedCost']['Amount'])
        data.append({'ds': date, 'y': round(amount, 2)})

    df = pd.DataFrame(data)
    df.to_csv('aws_cost_data.csv', index=False)
    print("✅ Saved AWS cost data to aws_cost_data.csv")

if __name__ == "__main__":
    get_daily_cost()
