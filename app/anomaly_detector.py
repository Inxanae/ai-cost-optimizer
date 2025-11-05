import pandas as pd
import numpy as np

def detect_anomalies(df):
    """
    Detect anomalies in daily cost using z-score method.
    df should have columns: ['ds', 'y']
    """
    data = df.copy()
    mean = data['y'].mean()
    std = data['y'].std()

    # Compute z-score
    data['z_score'] = (data['y'] - mean) / std
    threshold = 2.0  # Customize sensitivity (2 = moderate, 3 = strict)

    # Mark anomalies
    anomalies = data[np.abs(data['z_score']) > threshold]

    alerts = []
    for _, row in anomalies.iterrows():
        alerts.append(
            f"⚠️ Cost spike on {row['ds'].strftime('%Y-%m-%d')} — ₹{row['y']:.2f} (Z={row['z_score']:.2f})"
        )

    return anomalies, alerts

