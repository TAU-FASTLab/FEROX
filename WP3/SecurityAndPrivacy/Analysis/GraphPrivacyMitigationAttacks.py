import pandas as pd
import matplotlib.pyplot as plt

def generate_privacy_dataframe():
    """
    Creates and returns a DataFrame for privacy measures across FEROX components.
    """
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
            True, True, True, True, True, True, True, True, False,
            True, True, False
        ],
        "Complies with Data Minimization Principles": [True] * 32
    }
    return pd.DataFrame(data_privacy)

def calculate_privacy_statistics(df, measures):
    """
    Calculates the percentage of components that implement each privacy measure.
    """
    return [df[measure].mean() * 100 for measure in measures]

def plot_privacy_statistics(measures, percentages):
    """
    Plots the statistics for privacy measures implementation across components.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(measures, percentages, color="#4682b4", alpha=0.8)
    plt.xlabel("Privacy Measures", fontsize=12)
    plt.ylabel("Percentage of Components (%)", fontsize=12)
    plt.title("Privacy Measures Implementation Across FEROX Components", fontsize=14)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Annotate bars with percentages
    for i, value in enumerate(percentages):
        plt.text(i, value + 1, f"{value:.1f}%", ha="center", fontsize=10)

    plt.tight_layout()
    plt.savefig("Privacy_Measures_Statistics.png", dpi=300)
    plt.show()

# Main execution
if __name__ == "__main__":
    # Step 1: Generate the DataFrame
    privacy_df = generate_privacy_dataframe()

    # Step 2: Save the DataFrame to a CSV file
    privacy_df.to_csv("FEROX_Privacy_Summary.csv", index=False)

    # Step 3: Calculate statistics for privacy measures
    privacy_measures = [
        "Protects Against Data Retention Issues",
        "Ensures User Consent",
        "Applies Anonymization Techniques",
        "Limits Data Sharing with Third Parties",
        "Complies with Data Minimization Principles",
    ]
    privacy_percentages = calculate_privacy_statistics(privacy_df, privacy_measures)

    # Step 4: Plot and save the statistics
    plot_privacy_statistics(privacy_measures, privacy_percentages)
