import pandas as pd
import random
from datetime import datetime, timedelta

# Set start date (60 days ago)
start_date = datetime.now() - timedelta(days=60)

services = ['EC2', 'S3', 'RDS', 'Lambda', 'CloudFront']
data = []

for i in range(60):
    date = start_date + timedelta(days=i)
    for service in services:
        # Generate realistic daily cost patterns
        base_cost = {
            'EC2': random.uniform(10, 20),
            'S3': random.uniform(4, 8),
            'RDS': random.uniform(6, 12),
            'Lambda': random.uniform(1, 4),
            'CloudFront': random.uniform(2, 6)
        }
        cost = base_cost[service] + random.uniform(-1, 1)
        data.append([date.strftime('%Y-%m-%d'), service, round(cost, 2)])

df = pd.DataFrame(data, columns=['Date', 'Service', 'Cost'])
df.to_csv('data/aws_billing_mock.csv', index=False)

print("✅ Mock AWS billing data generated successfully!")
