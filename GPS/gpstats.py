import gpxpy
import gpxpy.gpx
from geopy.distance import geodesic
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pylab as plt
import matplotlib as mpl
import numpy as np
import scipy.stats as stats
import math

def statsAnalysis(file_path, vicenty_df, monthgps, daygps, time_of_day, gps_name):
    
    mean = vicenty_df.mean()
    median = vicenty_df.median()

    # Calculate the variance
    variance = vicenty_df.var()

    # Calculate the standard deviation
    std_dev = vicenty_df.std()

    # Calculate the standard error of the mean
    n = len(vicenty_df)
    standard_error = std_dev / math.sqrt(n)


    # Calculate the 95% Confidence Interval
    confidence_level = 0.95
    alpha = 1 - confidence_level
    z_critical = stats.norm.ppf(1 - alpha / 2)  # Get the z-critical value

    # Calculate the margin of error
    margin_of_error = z_critical * standard_error

    # Calculate the confidence interval
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)

    minimum = vicenty_df.min()  # Minimum value
    maximum = vicenty_df.max()  # Maximum value

    # Write to text file 
    with open(f"{file_path}/GPS/stats_analysis.txt", "a") as f:
        f.write(f"Year:2023, Day: {daygps}, Month: {monthgps},  Time of Day: {time_of_day}, GPS Name: {gps_name}\n")
        f.write(f"Minimum: {minimum}\n")
        f.write(f"Maximum: {maximum}\n")
        f.write(f"Mean: {mean}\n")
        f.write(f"Median: {median}\n")
        f.write(f"Variance: {variance}\n")
        f.write(f"Standard Deviation: {std_dev}\n")
        f.write(f"Standard Error: {standard_error}\n")
        f.write(f"95% Confidence Interval: {confidence_interval}\n")
        f.write(f"Margin of Error: {margin_of_error}\n")
        f.write("\n")  # Empty line for better readability

    vicenty_df_sorted = vicenty_df.sort_values()

    #vicenty_df_sorted['cumulative_count'] = vicenty_df_sorted.groupby('Vincenty_Error').cumcount() + 1  # Cumulative count per unique value
    leng = len(vicenty_df_sorted)
    relative_frequencies = vicenty_df_sorted.value_counts(normalize=True).sort_index()
    cdf = np.cumsum(relative_frequencies)
    #print(cdf)
    plt.figure(figsize=(10, 6))
    plt.plot(cdf.index, cdf.values, marker='o')
    plt.xlabel('Vicent Distance (m)')
    plt.ylabel('CDF')
    plt.title(f'Cumulative Distribution Function (CDF) of the Vicenty Error for -{gps_name}-{daygps}-{monthgps}-{time_of_day}')
    plt.grid(True)
    plt.savefig(f"{file_path}/GPS/{daygps}-{monthgps}-{time_of_day}/CDF_-{gps_name}-{daygps}-{monthgps}-{time_of_day}.png", dpi=1000)
    #plt.show()