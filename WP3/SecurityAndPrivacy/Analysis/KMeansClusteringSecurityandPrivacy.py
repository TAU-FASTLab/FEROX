# Rewriting the necessary code to reinitialize the environment

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Re-create the data for security and privacy measures
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

privacy_data = {
    "FEROX Component": security_data["FEROX Component"],
    "Protects Against Data Retention Issues": [True] * 32,
    "Ensures User Consent": [
        True, False, False, True, True, False, False, False, True, False, False, True, True, True, True, True, False, False, True, False, False, True, False, True, True, False, True, True, True, False, True, False
    ],
    "Applies Anonymization Techniques": [
        True, False, False, True, True, True, True, True, True, False, False, True, True, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True,  False, False, True, False
    ],
    "Limits Data Sharing with Third Parties": [
        True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, False, True, True, True, True, False, False, False, True,  False, False, True, False
    ],
    "Complies with Data Minimization Principles": [True] * 32
}

# Create DataFrames
ferox_components_df = pd.DataFrame(security_data)
privacy_df = pd.DataFrame(privacy_data)

# Calculate total security and privacy measures for each component
ferox_components_df["Total Security Measures"] = ferox_components_df.iloc[:, 1:].astype(int).sum(axis=1)
privacy_df["Total Privacy Measures"] = privacy_df.iloc[:, 1:].astype(int).sum(axis=1)

# Combine results into a single DataFrame
combined_measures_df = pd.concat(
    [ferox_components_df[["FEROX Component", "Total Security Measures"]],
     privacy_df[["Total Privacy Measures"]]],
    axis=1
)

# Perform KMeans clustering
scaler = StandardScaler()
data_to_cluster = combined_measures_df[["Total Security Measures", "Total Privacy Measures"]]
scaled_data = scaler.fit_transform(data_to_cluster)

kmeans = KMeans(n_clusters=3, random_state=42)
combined_measures_df["Cluster"] = kmeans.fit_predict(scaled_data)

# Group components by clusters
clustered_components = combined_measures_df.groupby("Cluster")["FEROX Component"].apply(list)

# Display components by cluster
clustered_components_dict = clustered_components.to_dict()
clustered_components_dict
