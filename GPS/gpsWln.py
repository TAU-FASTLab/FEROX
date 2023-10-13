from geopy.distance import geodesic
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pylab as plt
import month2Number
import seaborn as sns


# def loadGPXFile(yeargps, monthgps, daygps, hourgps, minutegps, secondgps, time_of_day, totaldurationhour,
# totaldurationminutes, totaldurationseconds):

def gpsWlnData (file_path, gpx_df, yeargps, monthgps, daygps, hourgps, minutegps, secondgps, time_of_day, gps_name, sampling_interval):
    # Initialize an empty DataFrame
    df_minifinder = pd.DataFrame(columns=['Latitude', 'Longitude','Timestamp'])
    df_minifinder['Timestamp'] = pd.to_datetime(df_minifinder['Timestamp'])

    #initial_time = datetime.strptime('2023-07-25 10:58:01', '%Y-%m-%d %H:%M:%S')
    initial_time = datetime(year=yeargps, month=month2Number.month_to_number(monthgps), day=daygps, hour=hourgps, minute=minutegps, second=secondgps)

    # Sample interval of 30 seconds/60 sec/ 180 sec
    delta = timedelta(seconds=sampling_interval)

    # Read the Wialon file into the wialon_data array
    

    file_path_wln = f'{file_path}/GPS/{daygps}-{monthgps}-{time_of_day}/{gps_name}/{daygps}-{monthgps}-{time_of_day}-{gps_name}.wln'
    with open(file_path_wln, 'r') as wialon_file:
        wialon_data = wialon_file.readlines()

#    #  initial_time = datetime(year=yeargps, month=Month2Number.month_to_number(monthgps), day=daygps, hour=hourgps, minute=minutegps, second=secondgps)

    # Populate the DataFrame
    for index, line in enumerate(wialon_data):
        parts = line.split(';')
        longitude = float(parts[2])
        latitude = float(parts[3])
        
        # Generate the timestamp
        timestamp_minifinder = initial_time + index * delta
        #print(timestamp_minifinder)
        
        # Add to DataFrame
        new_row = pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude], 'Timestamp': [timestamp_minifinder]})
        df_minifinder = df_minifinder.dropna(how='all', axis=1)
        df_minifinder = pd.concat([df_minifinder, new_row], ignore_index=True)
        #df_minifinder = pd.concat({'timestamp': timestamp_minifinder, 'longitude': longitude, 'latitude': latitude}, ignore_index=True)

    df_minifinder['Timestamp'] = pd.to_datetime(df_minifinder['Timestamp']).dt.floor('S')
    gpx_df['Timestamp'] = pd.to_datetime(gpx_df['Timestamp']).dt.floor('S')

    #df_minifinder_gpx = pd.DataFrame(columns=['Timestamp'])

    # Find matching times
    #common_times = df_minifinder[df_minifinder['Timestamp'].isin(gpx_df['Timestamp'])]

    # Display common times
    #print(common_times)

    # Merge DataFrames on 'Timestamp'
    merged_df = pd.merge(df_minifinder, gpx_df, on='Timestamp', suffixes=('_df_minifinder', '_gpx_df'))
    merged_df = merged_df.query("Latitude_df_minifinder != 0.0 and Longitude_df_minifinder != 0.0")
    merged_df['Vincenty_Error'] = merged_df.apply(lambda row: geodesic((row['Latitude_df_minifinder'], row['Longitude_df_minifinder']), (row['Latitude_gpx_df'], row['Longitude_gpx_df'])).meters, axis=1)
    merged_df['gps_name'] = gps_name
    merged_df['daygps'] = daygps
    merged_df['monthgps'] = monthgps
    merged_df['time_of_day'] = time_of_day
    merged_df['sampling_interval'] = sampling_interval
    #print('merged_df')
    #print(merged_df)
    vicenty_df = merged_df['Vincenty_Error']
    vicenty_df=vicenty_df.astype(float)
 

    #-----------
        #for i, txt in enumerate(merged_df['Timestamp']):
    #   plt.annotate(f"Phone-{txt}", (merged_df['Longitude_gpx_df'].iloc[i], merged_df['Latitude_gpx_df'].iloc[i]))
        #for i, txt in enumerate(merged_df['Timestamp']):
    #   plt.annotate(f"df_minifinder-{txt}", (merged_df['Longitude_df_minifinder'].iloc[i], merged_df['Latitude_df_minifinder'].iloc[i]))
    # Plot MapMyFitness - PhoneApp coordinates
    # Plot GPS coordinates
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['Longitude_df_minifinder'], merged_df['Latitude_df_minifinder'], c='blue', label='GPS Minifinder')
    plt.scatter(merged_df['Longitude_gpx_df'], merged_df['Latitude_gpx_df'], c='red', label='Phone App')
    plt.title(f'Coordinates Over Time-{gps_name}GPS-{daygps}-{monthgps}-{time_of_day}')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.grid(True)
    picture_file_path_coord = f"{file_path}/GPS/{daygps}-{monthgps}-{time_of_day}/CoordinatesOverTime-{gps_name}-{daygps}-{monthgps}-{time_of_day}.png"
    plt.savefig(picture_file_path_coord, dpi=1000)
    plt.close()
    #plt.show()
    #----------

   #----------- Plot Vicenty Error Line

    plt.figure(figsize=(10, 6))
    plt.plot(merged_df['Timestamp'], merged_df['Vincenty_Error'], marker='o', c='green')
    plt.xlabel('Timestamp')
    plt.ylabel('Vincenty Distance (meters)')
    plt.title(f'Vicenty Distance Over Time-{gps_name}GPS-{daygps}-{monthgps}-{time_of_day}')
    plt.grid(True)
    picture_file_path_coord = f"{file_path}/GPS/{daygps}-{monthgps}-{time_of_day}/VicentyDistance-{gps_name}-{daygps}-{monthgps}-{time_of_day}.png"
    plt.savefig(picture_file_path_coord, dpi=1000)
    plt.close()
    #plt.show()

    
    
    #----------- Plot Vicenty Error Histogram

    plt.figure(figsize=(10, 6))
    plt.hist(vicenty_df, edgecolor='blue', bins=20)
    plt.xlabel('Vicenty Error (m)')
    plt.ylabel('Number of Times')
    plt.grid(True)
    plt.title(f'Vicenty Error-{gps_name}GPS-{daygps}-{monthgps}-{time_of_day}')
    picture_file_path = f"{file_path}/GPS/{daygps}-{monthgps}-{time_of_day}/Histogram-VicentyError-{gps_name}-{daygps}-{monthgps}-{time_of_day}.png"
    plt.savefig(picture_file_path, dpi=1000)
    plt.close()
    #plt.show()
    #----------

    #sns.boxplot(x=merged_df['gps_name'], y=merged_df['Vincenty_Error'])
    #plt.title(f'Box Plot of VicentyError -{gps_name}-{daygps}-{monthgps}-{time_of_day} ')
    #plt.show()


    return vicenty_df, merged_df
