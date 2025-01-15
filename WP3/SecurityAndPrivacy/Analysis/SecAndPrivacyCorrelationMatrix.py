import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import numpy as np
#import plotly.graph_objects as go


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

# Standardize the data for clustering
scaler = StandardScaler()
data_to_cluster = combined_measures_df[["Total Security Measures", "Total Privacy Measures"]]
scaled_data = scaler.fit_transform(data_to_cluster)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
combined_measures_df["Cluster"] = kmeans.fit_predict(scaled_data)

# Scatter plot to visualize clusters
plt.figure(figsize=(10, 6))
for cluster in combined_measures_df["Cluster"].unique():
    cluster_data = combined_measures_df[combined_measures_df["Cluster"] == cluster]
    plt.scatter(
        cluster_data["Total Security Measures"],
        cluster_data["Total Privacy Measures"],
        label=f"Cluster {cluster}",
        s=100
    )

plt.xlabel("Total Security Measures", fontsize=12)
plt.ylabel("Total Privacy Measures", fontsize=12)
plt.title("Cluster Analysis of Security and Privacy Measures", fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Prepare data for correlation analysis
# Combine all security and privacy measures into one DataFrame
all_measures_df = pd.concat(
    [ferox_components_df.iloc[:, 1:].astype(int), privacy_df.iloc[:, 1:].astype(int)],
    axis=1
)

# Calculate the correlation matrix
correlation_matrix = all_measures_df.corr()

# Plot the correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    cbar_kws={"label": "Correlation Coefficient"}
)
plt.title("Correlation Matrix of Security and Privacy Measures", fontsize=16, pad=20)
plt.tight_layout()
plt.show()

# Calculate correlations (ensure numeric data)
correlation_matrix = all_measures_df.corr()

# Define a custom color map to highlight no meaningful correlation
custom_cmap = sns.diverging_palette(240, 10, as_cmap=True)
no_corr_color = "gray"

# Mask for blank cells
mask = np.isnan(correlation_matrix)

# Create the heatmap
plt.figure(figsize=(10, 8))
ax = sns.heatmap(
    correlation_matrix, 
    cmap=custom_cmap, 
    annot=True, 
    fmt=".2f", 
    mask=mask, 
    cbar_kws={"label": "Correlation Coefficient"}, 
    vmin=-1, vmax=1
)

# Add color for the mask (blank cells)
for (i, j), val in np.ndenumerate(correlation_matrix):
    if mask[i, j]:  # Check if the cell is masked
        ax.add_patch(plt.Rectangle((j, i), 1, 1, color=no_corr_color, ec=None))

plt.title("Correlation Matrix of Security and Privacy Measures", fontsize=16, pad=20)
plt.xlabel("Measures", fontsize=12)
plt.ylabel("Measures", fontsize=12)

plt.xticks(rotation=45, ha="right", fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
