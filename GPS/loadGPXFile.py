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
import month2Number

#df_MapMyFitness = loadGPXFile.loadGPXFile(2023, 'July', 25, 'July', 10, 58, 1, 'Morning', 1, 51, 24)

def loadGPXFile(file_path, yeargps, monthgps, daygps, hourgps, minutegps, secondgps, time_of_day, totaldurationhour, totaldurationminutes, totaldurationseconds):
    file_path = f"{file_path}/GPS/{daygps}-{monthgps}-{time_of_day}/{daygps}-{monthgps}-{time_of_day}.gpx"
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Iterate through tracks and segments and print lat and long
    #for track in gpx.tracks:
    #   for segment in track.segments:
    #      for point in segment.points:
    #         print(f'Latitude: {point.latitude}, Longitude: {point.longitude}')

    # Initialize empty lists to hold the latitude and longitude values
    gpx_latitudes = []
    gpx_longitudes = []

    # Loop through tracks, segments, and points to get the coordinates
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                gpx_latitudes.append(point.latitude)
                gpx_longitudes.append(point.longitude)

    # Create a DataFrame for GPX data

    gpx_df = pd.DataFrame({
        'Latitude': gpx_latitudes,
        'Longitude': gpx_longitudes
    })
        #the initial_time is set to 10:58 on 25th July 2023, and total_duration is set to 1 hour, 51 minutes, and 24 seconds. 
    # time_increment is calculated as the total duration divided by the number of samples in the DataFrame, 
    # and then a list of timestamps is generated to match the DataFrame's length.

    #-----------------------------------------------
    # Initialize the initial time as 10:58 on 25th July 2023

    initial_time = datetime(year=yeargps, month=Month2Number.month_to_number(monthgps), day=daygps, hour=hourgps, minute=minutegps, second=secondgps)
    # Create a time delta of 1 hour, 51 minutes, and 24 seconds
    total_duration = timedelta(hours=totaldurationhour, minutes=totaldurationminutes, seconds=totaldurationseconds)

    # Calculate the time increment between each sample
    # total_seconds() returns the total duration in seconds
    # Dividing by the length of DataFrame to find the interval between each timestamp
    time_increment = timedelta(seconds=(total_duration.total_seconds() / len(gpx_df)))

    # Generate a list of timestamps starting from the initial_time and incrementing by time_increment
    timestamps = [initial_time + i*time_increment for i in range(len(gpx_df))]

    # Add the generated timestamps to your DataFrame
    gpx_df['Timestamp'] = timestamps

    # Display the DataFrame
    #print(gpx_df)
    return gpx_df