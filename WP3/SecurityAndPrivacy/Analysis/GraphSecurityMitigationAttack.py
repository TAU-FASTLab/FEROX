# Security Mitigation graph code
import pandas as pd
import matplotlib.pyplot as plt

# Data for all FEROX components and attack mitigations
data = {
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

# Create the DataFrame
ferox_components_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
ferox_components_df.to_csv("FEROX_Components_Security_Summary.csv", index=False)

# Calculate the percentage of components mitigating each attack
total_components = len(ferox_components_df)
attack_categories = [
    "Mitigates Unauthorized Access",
    "Mitigates Man-in-the-Middle (MitM)",
    "Mitigates Data Tampering",
    "Mitigates Replay Attacks",
    "Mitigates GPS Spoofing",
    "Mitigates Denial of Service (DoS)",
]

# Count the mitigations
mitigation_percentages = [
    ferox_components_df[category].sum() / total_components * 100
    for category in attack_categories
]

# Create a bar chart for the statistics
plt.figure(figsize=(10, 6))
plt.bar(attack_categories, mitigation_percentages, alpha=0.8, color="purple")
plt.xlabel("Attack Types", fontsize=12)
plt.ylabel("Mitigation Percentage (%)", fontsize=12)
plt.title("Attack Mitigation Statistics Across FEROX Components", fontsize=14, pad=20)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Annotate the bars with percentage values
for i, value in enumerate(mitigation_percentages):
    plt.text(i, value + 1, f"{value:.1f}%", ha="center", fontsize=10)

# Adjust the layout to avoid overlapping
plt.tight_layout()
plt.savefig("AttackTypesPercentage.png", dpi=300)

# Display the graph
plt.show()

# Create a plot to visualize the number of components mitigating specific attacks

# Count the number of components mitigating each attack
attack_counts = [
    ferox_components_df[category].sum() for category in attack_categories
]

# Create a bar chart for the number of components mitigating specific attacks
plt.figure(figsize=(10, 6))
plt.bar(attack_categories, attack_counts, color="teal", alpha=0.8)
plt.xlabel("Attack Types", fontsize=12)
plt.ylabel("Number of Components Mitigating", fontsize=12)
plt.title("Number of FEROX Components Mitigating Specific Attacks", fontsize=14, pad=20)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Annotate the bars with the number of components
for i, count in enumerate(attack_counts):
    plt.text(i, count + 0.5, f"{count}", ha="center", fontsize=10)

# Adjust layout for clarity
plt.tight_layout()
plt.savefig("AttackTypes.png", dpi=300)

# Display the plot
plt.show()
