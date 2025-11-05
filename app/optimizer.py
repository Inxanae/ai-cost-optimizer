import pandas as pd

def suggest_optimizations(df):
    suggestions = []

    high_cost_services = df.groupby('Service')['Cost'].sum().sort_values(ascending=False)
    top_service = high_cost_services.index[0]
    top_cost = high_cost_services.iloc[0]

    suggestions.append(f"⚡ High spending on {top_service}: ₹{top_cost:.2f}. Consider right-sizing instances.")
    if 'EC2' in df['Service'].values:
        suggestions.append("💤 Some EC2 instances might be idle — schedule auto-stop for low-usage hours.")
    if 'S3' in df['Service'].values:
        suggestions.append("🧹 Enable S3 lifecycle policies to delete unused objects.")
    if 'Lambda' in df['Service'].values:
        suggestions.append("🧠 Consider consolidating Lambda functions to reduce invocation cost.")

    total_cost = df['Cost'].sum()
    suggestions.append(f"💰 Total month cost: ₹{total_cost:.2f}")
    
    return suggestions
