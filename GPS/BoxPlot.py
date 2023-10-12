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
file_path = f'...'
# Filter DataFrame based on specific day, month, year, and time of day
df_merged_total = pd.read_csv('df_merged_total.csv')
days = [25, 26, 27]
times_of_day = ['Morning', 'Afternoon']
month = 'July'

# Loop through each day and time_of_day
for day in days:
    for time_of_day in times_of_day:
        if (day == 25 and (time_of_day == 'Afternoon' or time_of_day == 'Morning')) or \
        (day == 27 and (time_of_day == 'Afternoon' or time_of_day == 'Morning')) or \
        (day == 26 and time_of_day == 'Afternoon'):
            filtered_df = df_merged_total[
                (df_merged_total['daygps'] == day) &
                (df_merged_total['monthgps'] == month) &
                (df_merged_total['time_of_day'] == time_of_day)
            ]
            print(filtered_df[['daygps','monthgps','time_of_day','gps_name','Vincenty_Error']])
            print(filtered_df['Vincenty_Error'].describe())
            plt.figure(figsize=(10, 6))  # Create a new figure for each boxplot
            sns.boxplot(x=filtered_df['gps_name'], y=filtered_df['Vincenty_Error'], data=filtered_df, notch=True)
            plt.yscale('log')
            plt.title(f'Vicenty Error Boxplot-{day}-{month}-{time_of_day}')
            plt.savefig(f"{file_path}/BoxPlotLog_-{day}-{month}-{time_of_day}.png", dpi=1000)
            plt.show()
            plt.close()

