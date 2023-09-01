# Disclaimer: Code not compiled yet
#https://stackoverflow.com/questions/67106853/how-to-do-point-biserial-correlation-for-multiple-columns-in-one-iteration

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Row example of .wln file 
#REG;1690271769;31.09046;62.739162;0;154;ALT:164.3;
#SATS:5,signal:0,gps_module:0,over_speed:0,fall_alarm:0,battery:0,motion_alarm:0,move_alarm:0,gsm_csq:7,battery_level:97,sats_in_view:14;;;;

#Read the wln file data in a DataFrame and the parse it in a way to get the values separated in a format of Key, value

GPSWln_data = pd.read_csv('folder to the wln file', sep=';', header=None, names=["REG", "Coord1", "Coord2", "Coord3", "Coord4", "Coord5", "Coord6", "value", "Coord7", "Coord8", "Coord9", "Coord10"])
df = pd.DataFrame()
# GPSWln_data['value'] contains the data that I am interested in 
for gps_x in range(len(GPSWln_data['value'])):
    array_GPSvalue = GPSWln_data['value'][gps_x]
    GPS_list = array_GPSvalue.split(",")
    data_dict={}
    for item in GPS_list:
        key, value = item.split(':')
        data_dict[key]=value
    df=df.append(data_dict, ignore_index=True)
    

#correlationpointbiseral=stats.pointbiserialr(df["signal"], df["SATS"])
correlationpointbiseral = stats.pointbiserialr(df["signal"].astype(float), df["SATS"].astype(float))
#pbDF=df.corrwith(df['signal'].astype('float'), method=stats.pointbiserialr)
# Pearson correlation coefficient matrix
correlationcoeficient = df.corr(method='pearson')
#coreelationparson = stats.pearsonr(df)
#DFcpearson=df.corr(method ='pearson')
#correlationcoeficient = np.corrcoef(df)

print("The correlation biseral is: ", correlationpointbiseral)
print("\n The correlation by pearson is: ", coreelationparson)
#print("\n The correlation coeficient is: \n", correlationcoeficient)
#print("dataframe correlation with point biseral", pbDF)

# Set the style for seaborn plots
sns.set_style("whitegrid")

# Scatter plot for 'signal' and 'SATS'
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="signal", y="SATS")
plt.title("Scatter plot of 'signal' vs 'SATS'")
plt.show()

# Heatmap for the correlation coefficient matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlationcoeficient, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Coefficient Matrix Heatmap")
plt.show()

