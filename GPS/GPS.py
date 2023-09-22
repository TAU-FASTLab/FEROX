import gpxpy
import gpxpy.gpx
from geopy.distance import geodesic
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pylab as plt
import matplotlib as mpl


# Load the GPX file
with open('C:/Users/phmaro/OneDrive - TUNI.fi/Documents/Programming/route5649825475.gpx', 'r') as gpx_file:
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

print(gpx_df)

#the initial_time is set to 10:58 on 25th July 2023, and total_duration is set to 1 hour, 51 minutes, and 24 seconds. 
# time_increment is calculated as the total duration divided by the number of samples in the DataFrame, 
# and then a list of timestamps is generated to match the DataFrame's length.



#-----------------------------------------------
# Initialize initial time (Replace these initial hours and minutes with yours)
#initial_hour = 10
#initial_minute = 58

# Initialize the initial time as 10:58 on 25th July 2023
initial_time = datetime(year=2023, month=7, day=25, hour=10, minute=58, second=1)

# Create a time delta of 1 hour, 51 minutes, and 24 seconds
total_duration = timedelta(hours=1, minutes=51, seconds=24)

# Calculate the time increment between each sample
# total_seconds() returns the total duration in seconds
# Dividing by the length of DataFrame to find the interval between each timestamp
time_increment = timedelta(seconds=(total_duration.total_seconds() / len(gpx_df)))

# Generate a list of timestamps starting from the initial_time and incrementing by time_increment
timestamps = [initial_time + i*time_increment for i in range(len(gpx_df))]

# Add the generated timestamps to your DataFrame
gpx_df['Timestamp'] = timestamps

# Display the DataFrame
print(gpx_df)

#------------- WIALON Message---------------------------

# Initialize an empty DataFrame
df_minifinder = pd.DataFrame(columns=['Latitude', 'Longitude','Timestamp'])
df_minifinder['Timestamp'] = pd.to_datetime(df_minifinder['Timestamp'])

# Initial time at 10:58 (you can adjust the date and timezone)
initial_time = datetime.strptime('2023-07-25 10:58:01', '%Y-%m-%d %H:%M:%S')

# Sample interval of 30 seconds
delta = timedelta(seconds=30)

# Read the Wialon file into the wialon_data array
with open('C:/Users/phmaro/OneDrive - TUNI.fi/Documents/Programming/25JulyPinkForest.wln', 'r') as file:
    wialon_data = file.readlines()

# Populate the DataFrame
for index, line in enumerate(wialon_data):
    parts = line.split(';')
    longitude = float(parts[2])
    latitude = float(parts[3])
    
    # Generate the timestamp
    timestamp_minifinder = initial_time + index * delta
    print(timestamp_minifinder)
    
    # Add to DataFrame
    new_row = pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude], 'Timestamp': [timestamp_minifinder]})
    df_minifinder = pd.concat([df_minifinder, new_row], ignore_index=True)
    #df_minifinder = pd.concat({'timestamp': timestamp_minifinder, 'longitude': longitude, 'latitude': latitude}, ignore_index=True)

# Show the DataFrame
print("Minifinder")
print(df_minifinder)
print("gpx_df")
print(gpx_df)

df_minifinder['Timestamp'] = pd.to_datetime(df_minifinder['Timestamp']).dt.floor('S')
gpx_df['Timestamp'] = pd.to_datetime(gpx_df['Timestamp']).dt.floor('S')

#print("Minifinder")
#print(df_minifinder)
#print("gpx_df")
#print(gpx_df)

#df_minifinder_gpx = pd.DataFrame(columns=['Timestamp'])

# Find matching times
#common_times = df_minifinder[df_minifinder['Timestamp'].isin(gpx_df['Timestamp'])]

# Display common times
#print(common_times)

# Merge DataFrames on 'Timestamp'
merged_df = pd.merge(df_minifinder, gpx_df, on='Timestamp', suffixes=('_df_minifinder', '_gpx_df'))
merged_df['Vincenty_Error'] = merged_df.apply(lambda row: geodesic((row['Latitude_df_minifinder'], row['Longitude_df_minifinder']), (row['Latitude_gpx_df'], row['Longitude_gpx_df'])).meters, axis=1)

print(merged_df)

plt.figure(figsize=(10, 6))
plt.plot(merged_df['Timestamp'], merged_df['Vincenty_Error'], marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Vincenty Distance (meters)')
plt.title('Vincenty Distance Over Time - Pink July 25 Morning')
plt.grid(True)
plt.savefig("VicentyPink25JulyFirst.png", dpi=1000)
plt.show()

# Create a figure
plt.figure(figsize=(10, 6))

# Plot Set A coordinates
plt.scatter(merged_df['Longitude_df_minifinder'], merged_df['Latitude_df_minifinder'], c='blue', label='GPS Minifinder')
#for i, txt in enumerate(merged_df['Timestamp']):
 #   plt.annotate(f"df_minifinder-{txt}", (merged_df['Longitude_df_minifinder'].iloc[i], merged_df['Latitude_df_minifinder'].iloc[i]))

# Plot Set B coordinates
plt.scatter(merged_df['Longitude_gpx_df'], merged_df['Latitude_gpx_df'], c='red', label='Phone App')
#for i, txt in enumerate(merged_df['Timestamp']):
 #   plt.annotate(f"Phone-{txt}", (merged_df['Longitude_gpx_df'].iloc[i], merged_df['Latitude_gpx_df'].iloc[i]))

# Label the plot
plt.title('Coordinates Over Time - Pink July 25 Morning')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(True)
plt.savefig("GPSLatitudeLongitude-25JulyMorning.png", dpi=1000)
# Show the plot
plt.show()


# Initialize a datetime object with your chosen initial time
#initial_time = datetime(year=2023, month=7, day=25, hour=initial_hour, minute=initial_minute, second=0, microsecond=0)

# Calculate time increment in seconds (59 samples per minute means each sample is ~1.01695 seconds apart)
#time_increment = timedelta(seconds=(60 / 59))

# Generate a list of timestamps starting from the initial_time and incrementing by time_increment
#timestamps = [initial_time + i*time_increment for i in range(len(gpx_df))]

# Add the generated timestamps to your DataFrame
#gpx_df['Timestamp'] = timestamps

# Display the DataFrame
#print(gpx_df)


#coord1 = (40.7128, -74.0060)  # New York
#coord2 = (34.0522, -118.2437)  # Los Angeles

#distance = geodesic(coord1, coord2).kilometers
#print("Distance Error in km:", distance)
