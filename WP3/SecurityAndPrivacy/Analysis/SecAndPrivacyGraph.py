# Re-creating the data for security and privacy measures for FEROX components
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Data for security measures
security_data = {
    "FEROX Component": [
        "LWD Task Manager & LWD Action Clients",
        "OperatorApp Backend: ROI Clustering",
        "API Integration – Weather API",
        "Human-HWD Task Manager & HWD Action Clients",
        "PickerApp Backend: WatchDog Request",
        "Point cloud Postprocessing",
        "Multi-Layer Grid Map",
        "Image Postprocessing",
        "Predictive Crop and Modelling Yield",
        "GPS Minifinder Back-End",
        "Server for Sensor Dragino (Temperature & Humidity)",
        "Interactive Yield",
        "Picking Planner",
        "Human Activity Recognition",
        "Integration with Wearables (BLE)",
        "Interactive ROI Definition",
        "Progress Monitoring",
        "UAV Homing",
        "Deep Forestry Light-weight Drone",
        "Scout v2",
        "DJI Mavic 2 Pro",
        "Holybro Pixhawk x500 v2",
        "DJI Mavic 3 Multispectral",
        "Deep Forestry Heavy-weight Drone",
        "GPS Minifinder",
        "Movesense",
        "Tobii Pro Glass",
        "Empatica Watch",
        "Dragino (Temp. & Humd. Sensor)",
        "WiFi (Drones <-> Local Server)",
        "BLE (Wearables Sensor <-> Smartphone)",
        "NB-IoT (Environmental Sensor <-> local server)"
    ],
    "Mitigates Unauthorized Access": [True] * 32,
    "Mitigates Man-in-the-Middle (MitM)": [True] * 32,
    "Mitigates Data Tampering": [True] * 32,
    "Mitigates Replay Attacks": [
        False, False, False, False, True, True, False, False, False, True, False,
        False, True, False, True, False, False, False, True, True, True, True, True,
        True, False, False, False, True, False, True, True, True
    ],
    "Mitigates GPS Spoofing": [
        False, False, False, False, False, True, False, False, False, True, False,
        False, True, False, True, False, False, True, True, True, True, True,
        True, True, True, True, False, True, False, False, True, False
    ],
    "Mitigates Denial of Service (DoS)": [
        False, True, True, True, True, True, False, False, False, True, True,
        False, True, False, True, False, True, False, True, True, True, True,
        True, True, False, False, False, True, True, True, True, True
    ]
}

# Data for privacy measures
privacy_data = {
    "FEROX Component": security_data["FEROX Component"],
    "Protects Against Data Retention Issues": [True] * 32,
    "Ensures User Consent": [
        True, True, False, True, True, False, False, False, True, True,
         False, True, True, True, True, False, False, False, False, 
         False, False, False, False, True, True, True, True, True, 
         False, True, True, False
    ],
    "Applies Anonymization Techniques": [
        True, True, False, True, True, True, True, True, True, 
        False, False, True, True, True, True, False, False, False, 
        True, True, True, True, True, True, False, False, True, True,
        False, True, True, False
    ],
    "Limits Data Sharing with Third Parties": [
        True, True, False, True, True, True, True, True, True, True, 
        False, True, True, True, True, False, False, False, True, True, 
        True, True, True, True, True, True, True, True,  False, 
        True, True, False
    ],
    "Complies with Data Minimization Principles": [True] * 32
}

# Create DataFrames
ferox_components_df = pd.DataFrame(security_data)
privacy_df = pd.DataFrame(privacy_data)

# Calculate total security and privacy measures for each component
ferox_components_df["Total Security Measures"] = ferox_components_df.iloc[:, 1:].sum(axis=1)
privacy_df["Total Privacy Measures"] = privacy_df.iloc[:, 1:].sum(axis=1)

# Combine results into a single DataFrame
stacked_data = pd.DataFrame({
    "FEROX Component": ferox_components_df["FEROX Component"],
    "Security Measures": ferox_components_df["Total Security Measures"],
    "Privacy Measures": privacy_df["Total Privacy Measures"]
})

# Plot the stacked bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.8
x = np.arange(len(stacked_data["FEROX Component"]))

plt.bar(x, stacked_data["Security Measures"], width=bar_width, label="Security Measures", color="skyblue")
plt.bar(x, stacked_data["Privacy Measures"], width=bar_width, bottom=stacked_data["Security Measures"], label="Privacy Measures", color="orange")

# Add labels and title
plt.xlabel("FEROX Components", fontsize=12)
plt.ylabel("Number of Measures Implemented", fontsize=12)
plt.title("Comparison of Security and Privacy Measures Across FEROX Components", fontsize=14)
plt.xticks(x, stacked_data["FEROX Component"], rotation=90, fontsize=10)
plt.legend()

# Adjust layout to prevent overlap
plt.tight_layout()
plt.savefig("SecurityPrivacyMeasures_v3.png", dpi=300)

# Show the chart
plt.show()
