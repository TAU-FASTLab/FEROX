import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read the table into a pandas DataFrame.
df = pd.read_csv('ferox_security_table.csv')

# 2. Inspect the DataFrame structure.
print(df.head())
print(df.info())

# 3. Suppose you have columns like:

# Count how many times each SecurityMeasure appears.
security_counts = df['SecurityMeasure'].value_counts()
print(security_counts)

# Plot a simple bar chart.
plt.figure(figsize=(8,6))
security_counts.plot(kind='bar')
plt.title("Frequency of Security Measures")
plt.xlabel("Security Measure")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Group by risk level (if you have a column like "RiskLevel")
if 'RiskLevel' in df.columns:
    risk_counts = df.groupby('RiskLevel')['Component'].count()
    print(risk_counts)

    # Visualize risk distribution.
    plt.figure(figsize=(8,6))
    risk_counts.plot(kind='bar', color='orange')
    plt.title("Components by Risk Level")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Components")
    plt.tight_layout()
    plt.show()

# Stacked bar or heatmap for Security vs. Privacy
# If you have columns like "SecurityMeasure" and "PrivacyMeasure"
if 'SecurityMeasure' in df.columns and 'PrivacyMeasure' in df.columns:
    cross_tab = pd.crosstab(df['SecurityMeasure'], df['PrivacyMeasure'])
    print(cross_tab)

    # Heatmap visualization
    plt.figure(figsize=(10,8))
    sns.heatmap(cross_tab, annot=True, cmap="YlGnBu", fmt="d")
    plt.title("Security vs Privacy Measures in FEROX")
    plt.xlabel("Privacy Measure")
    plt.ylabel("Security Measure")
    plt.show()
