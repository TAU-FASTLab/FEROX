import pandas as pd
import matplotlib.pyplot as plt

# Sample data for privacy measures in FEROX components (based on provided information)
data_privacy = {
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
        "BLE (Sensor <-> Smartphone)",
        "NB-IoT (Temp. Sensor <-> local server)"
    ],
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

# Create DataFrame
privacy_df = pd.DataFrame(data_privacy)

# Save the privacy table to a CSV file
privacy_df.to_csv("FEROX_Privacy_Summary.csv", index=False)

# Calculate statistics for privacy measures
privacy_measures = [
    "Protects Against Data Retention Issues",
    "Ensures User Consent",
    "Applies Anonymization Techniques",
    "Limits Data Sharing with Third Parties",
    "Complies with Data Minimization Principles",
]

privacy_percentages = [
    privacy_df[measure].sum() / len(privacy_df) * 100 for measure in privacy_measures
]

# Plotting statistics
plt.figure(figsize=(10, 6))
plt.bar(privacy_measures, privacy_percentages, color = "#4682b4" , alpha=0.8)
plt.xlabel("Privacy Measures", fontsize=12)
plt.ylabel("Percentage of Components (%)", fontsize=12)
plt.title("Privacy Measures Implementation Across FEROX Components", fontsize=14)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Annotate the bars with percentages
for i, value in enumerate(privacy_percentages):
    plt.text(i, value + 1, f"{value:.1f}%", ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("PrivacyTypesPercentage_v3.png", dpi=300)

# Display the plot
plt.show()
