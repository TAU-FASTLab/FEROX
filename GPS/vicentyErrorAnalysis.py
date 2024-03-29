import pandas as pd
import loadGPXFile
import gpsWln
import gpstats
import time
import statsFiletxt2csv
import seaborn as sns
import matplotlib.pylab as plt
import matplotlib as mpl

# GPS Minifinder data starting time, considering the duration from MapMyFitness App, as follows:
#25 July Morning tracking GPS Position from 10:58:01 during 1h 50 minutes and 24 seconds, collecting Raspberry in Thick Forest
#25 July Afternoon tracking GPS Position from 14:38:22 during 1h  7minutes and 47 seconds, collecting Cloudberry in Swamp Area
#26 July Afternoon tracking GPS Position from 14:05:23 during 1 h 17 minutes and 34 seconds, collecting Cloudberry in Swamp Area
#27 July Morning tracking GPS Position from 10:14:22 during 2 h 6 minutes and 12 seconds, collecting Raspberry in Thick Forest
#27 July Afternoon tracking GPS Position from 13:54:07 during 1 h 32 minutes and 49 seconds, collecting Raspberry in Thick Forest

dataGPS = [[2023, 'July', 25, 'Morning', 'Pink', 10, 58, 1, 30, 1, 50, 24], 
           [2023, 'July', 25, 'Morning', 'Blue', 10, 58, 1, 30, 1, 50, 24], 
           [2023, 'July', 25, 'Morning', 'White', 10, 58, 1, 60, 1, 50, 24],
           [2023, 'July', 25, 'Morning', 'Green', 10, 58, 1, 60, 1, 50, 24],
           [2023, 'July', 25, 'Morning', 'Black1', 10, 58, 1, 180, 1, 50, 24],
           [2023, 'July', 25, 'Morning', 'Black2', 10, 58, 1, 180, 1, 50, 24],
           [2023, 'July', 25, 'Afternoon', 'Pink', 14, 38, 22, 30, 1, 7, 47],
           [2023, 'July', 25, 'Afternoon', 'Blue', 14, 38, 22, 30, 1, 7, 47], 
           [2023, 'July', 25, 'Afternoon', 'White', 14, 38, 22, 60, 1, 7, 47],
           [2023, 'July', 25, 'Afternoon', 'Green', 14, 38, 22, 60, 1, 7, 47],
           [2023, 'July', 25, 'Afternoon', 'Black1', 14, 38, 22, 180, 1, 7, 47],
           [2023, 'July', 25, 'Afternoon', 'Black2', 14, 38, 22, 180, 1, 7, 47],
           [2023, 'July', 26, 'Afternoon', 'Pink', 14, 5, 23, 30, 1, 17, 34],
           [2023, 'July', 26, 'Afternoon', 'Blue', 14, 5, 23, 30, 1, 17, 34], 
           [2023, 'July', 26, 'Afternoon', 'White', 14, 5, 23, 60, 1, 17, 34],
           [2023, 'July', 26, 'Afternoon', 'Green', 14, 5, 23, 60, 1, 17, 34],
           [2023, 'July', 26, 'Afternoon', 'Black1', 14, 5, 23, 180, 1, 17, 34],
           [2023, 'July', 26, 'Afternoon', 'Black2', 14, 5, 23, 180, 1, 17, 34],
           [2023, 'July', 27, 'Morning', 'Pink', 10, 14, 22, 30, 2, 6, 12],
           [2023, 'July', 27, 'Morning', 'Blue', 10, 14, 22, 30, 2, 6, 12], 
           [2023, 'July', 27, 'Morning', 'White', 10, 14, 22, 60, 2, 6, 12],
           [2023, 'July', 27, 'Morning', 'Green', 10, 14, 22, 60, 2, 6, 12],
           [2023, 'July', 27, 'Morning', 'Black1', 10, 14, 22, 180, 2, 6, 12],
           [2023, 'July', 27, 'Morning', 'Black2', 10, 14, 22, 180, 2, 6, 12],
           [2023, 'July', 27, 'Afternoon', 'Pink', 13, 54, 7, 30, 1, 32, 49],
           [2023, 'July', 27, 'Afternoon', 'Blue', 13, 54, 7, 30, 1, 32, 49], 
           [2023, 'July', 27, 'Afternoon', 'White', 13, 54, 7, 60, 1, 32, 49],
           [2023, 'July', 27, 'Afternoon', 'Green', 13, 54, 7, 60, 1, 32, 49],
           [2023, 'July', 27, 'Afternoon', 'Black1', 13, 54, 7, 180, 1, 32, 49],
           [2023, 'July', 27, 'Afternoon', 'Black2', 13, 54, 7, 180, 1, 32, 49]]

# assign into a dataframe the data to iterate from the different GPSs
df_GPSAnalysis = pd.DataFrame(dataGPS, columns=['Year', 'Month', 'Day','TimeOfDay', 'GPSName', 'Hour', 'Minute', 'Second', 'Time_Interval','MapMyFitnessHourDuration', 'MapMyFitnessMinutesDuration','MapMyFitnessSecondDuration'])

file_path = f'C:/...'
# Loop through the DataFrame rows
df_merged_total = pd.DataFrame()
for index, row in df_GPSAnalysis.iterrows():
    yeargps = row['Year']
    monthgps = row['Month']
    daygps = row['Day']
    time_of_day = row['TimeOfDay']
    gps_name = row['GPSName']
    hourgps = row['Hour']
    minutegps = row['Minute']
    secondgps = row['Second']
    time_interval = row['Time_Interval']
    totaldurationhour = row['MapMyFitnessHourDuration']
    totaldurationminutes = row['MapMyFitnessMinutesDuration']
    totaldurationseconds = row['MapMyFitnessSecondDuration']
    # loadGPXFile loads the GPX file from MapmyFitness App, using the time and the duration
    df_MapMyFitness = loadGPXFile.loadGPXFile(file_path, yeargps, monthgps, daygps, hourgps, minutegps, secondgps, time_of_day, totaldurationhour, totaldurationminutes, totaldurationseconds)
    time.sleep(5)
    # GPSWlnData parse the Wln files from GPS Minifinder and calculates the VicentyDistance between the positions from GPS Minifinder and MapMyFitness
    #df_vicentyDistance = gpsWln.gpsWlnData(file_path, df_MapMyFitness, yeargps, monthgps, daygps, hourgps, minutegps, secondgps, time_of_day, gps_name, time_interval)
    #time.sleep(5)
    df_vicentyDistance, df_merged_bygps = gpsWln.gpsWlnData(file_path, df_MapMyFitness, yeargps, monthgps, daygps, hourgps, minutegps, secondgps, time_of_day, gps_name, time_interval)
    #print(df_vicentyDistance)
    time.sleep(5)
    # StatsAnalysis calculates from the vicenty distance values the min, max, mean, median, variance, standard deviation, confidence interval 95%, Cumulative Distribution Function, 
    gpstats.statsAnalysis(file_path, df_vicentyDistance, monthgps, daygps, time_of_day, gps_name)
    df_merged_total = pd.concat([df_merged_total, df_merged_bygps], ignore_index=True)
    # StatsAnalysis calculates from the vicenty distance values the min, max, mean, median, variance, standard deviation, confidence interval 95%, Cumulative Distribution Function, 
    #gpstats.statsAnalysis(file_path, df_vicentyDistance,monthgps, daygps, time_of_day, gps_name)

df_merged_total.to_csv('df_merged_total.csv', index=False)  # Set index=False to avoid saving row indices

#This takes the txt generated with the statsiscally data and save it as csv 
statsFiletxt2csv.statsFileTxt2csv(file_path)
