import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read the table into a pandas DataFrame
df = pd.read_csv('ferox_security_table.csv')

# 2. Count the occurrences of each PrivacyMeasure
privacy_counts = df['PrivacyMeasure'].value_counts()
print("Frequency of Privacy Measures:")
print(privacy_counts)

# 3. Plot a bar chart of the privacy measure frequencies
plt.figure(figsize=(8,6))
privacy_counts.plot(kind='bar', color='green')  # You can choose any color you like
plt.title("Frequency of Privacy Measures")
plt.xlabel("Privacy Measure")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ########################
# Component,SecurityMeasure,PrivacyMeasure,RiskLevel
# Local Server,Encryption,Data Minimization,Medium
# Local Server,Access Control,Pseudonymization,Medium
# Cloud,Encryption,Anonymization,High
# Cloud,Intrusion Detection System,Pseudonymization,High
# Smartphone,2FA (Two-Factor Auth),Data Minimization,Medium
# UAV,Secure Firmware,Anonymization,High
# Picker Sensor,Firewall,Anonymization,Low
# Picker Sensor,Encryption,Data Minimization,Low
# Environmental Sensor,Access Control,Pseudonymization,Medium
# Environmental Sensor,Encryption,Anonymization,Medium