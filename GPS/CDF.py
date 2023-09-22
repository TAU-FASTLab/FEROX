import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import matplotlib as mpl
#try:
    #import matplotlib.pylab as plt
    #import matplotlib as mpl
#except Exception, e:
    #sys.stderr.write("Matplotlib is not available!")

# Row example of .wln file 
#REG;1690271769;31.09046;62.739162;0;154;ALT:164.3;
#SATS:5,signal:0,gps_module:0,over_speed:0,fall_alarm:0,battery:0,motion_alarm:0,move_alarm:0,gsm_csq:7,battery_level:97,sats_in_view:14;;;;

#Read the wln file data in a DataFrame and the parse it in a way to get the values separated in a format of Key, value

GPSWln_data = pd.read_csv('C:/.../25JulyPinkForest.wln', sep=';', header=None, names=["REG", "Coord1", "Coord2", "Coord3", "Coord4", "Coord5", "Coord6", "value", "Coord7", "Coord8", "Coord9", "Coord10"])
df = pd.DataFrame()
# GPSWln_data['value'] contains the data that I am interested in 
for gps_x in range(len(GPSWln_data['value'])):
    array_GPSvalue = GPSWln_data['value'][gps_x]
    GPS_list = array_GPSvalue.split(",")
    data_dict={}
    for item in GPS_list:
        key, value = item.split(':')
        data_dict[key]=value
    df_dictionary = pd.DataFrame([data_dict])
    df=pd.concat([df, df_dictionary], ignore_index=True)

df=df.astype(float)

plt.hist(df['SATS'], edgecolor='black', bins=20)
plt.xlabel('SATS')
plt.ylabel('Value')
plt.title('Histogram SATS Function')
plt.savefig("HistogramSATs.png", dpi=1000)
plt.show()

plt.hist(df['signal'], edgecolor='black', bins=20)
plt.xlabel('signal')
plt.ylabel('Value')
plt.title('Histogram signal Function')
plt.savefig("Histogramsignal.png", dpi=1000)
plt.show()

plt.hist(df['gsm_csq'], edgecolor='black', bins=20)
plt.xlabel('gsm_csq')
plt.ylabel('Value')
plt.title('Histogram gsm_csq Function')
plt.savefig("Histogramgsm_csq.png", dpi=1000)
plt.show()

plt.hist(df['sats_in_view'], edgecolor='black', bins=20)
plt.xlabel('sats_in_view')
plt.ylabel('Value')
plt.title('Histogram sats_in_view Function')
plt.savefig("Histogramsats_in_view.png", dpi=1000)
plt.show()

df_SATS_sorted = df.sort_values('SATS')

df_SATS_sorted['cumulative_count'] = df_SATS_sorted.groupby('SATS').cumcount() + 1  # Cumulative count per unique value
print(df_SATS_sorted['cumulative_count'])
print(df_SATS_sorted['SATS'].count())
df_SATS_sorted['cdfSATS'] = df_SATS_sorted['cumulative_count'] / df_SATS_sorted['SATS'].count()  # Divide by total number of observations
print(df_SATS_sorted['cdfSATS'].count())

print(df_SATS_sorted)

plt.step(df_SATS_sorted['SATS'], df_SATS_sorted['cdfSATS'], where='post')
#plt.plot(df['SATS'], df['cdf'])
plt.xlabel('SATS')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function')
plt.savefig("CDFSATs.png", dpi=1000)
plt.show()

df_signal_sorted = df.sort_values('signal')

df_signal_sorted['cumulative_count'] = df_signal_sorted.groupby('signal').cumcount() + 1  # Cumulative count per unique value
print(df_signal_sorted['cumulative_count'])
print(df_signal_sorted['signal'].count())
df_signal_sorted['cdfsignal'] = df_signal_sorted['cumulative_count'] / df_signal_sorted['signal'].count()  # Divide by total number of observations
print(df_signal_sorted['cdfsignal'].count())

print(df_signal_sorted)

plt.step(df_signal_sorted['signal'], df_signal_sorted['cdfsignal'], where='post')
#plt.plot(df['SATS'], df['cdf'])
plt.xlabel('Signal')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function')
plt.savefig("CDFSignal.png", dpi=1000)
plt.show()

df_gsm_csq_sorted = df.sort_values('gsm_csq')

df_gsm_csq_sorted['cumulative_count'] = df_gsm_csq_sorted.groupby('gsm_csq').cumcount() + 1  # Cumulative count per unique value
print(df_gsm_csq_sorted['cumulative_count'])
print(df_gsm_csq_sorted['gsm_csq'].count())
df_gsm_csq_sorted['cdfgsm_csq'] = df_gsm_csq_sorted['cumulative_count'] / df_gsm_csq_sorted['gsm_csq'].count()  # Divide by total number of observations
print(df_gsm_csq_sorted['cdfgsm_csq'].count())

print(df_gsm_csq_sorted)

plt.step(df_gsm_csq_sorted['gsm_csq'], df_gsm_csq_sorted['cdfgsm_csq'], where='post')
#plt.plot(df['SATS'], df['cdf'])
plt.xlabel('gsm_csq')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function')
plt.savefig("CDFgsm_csq.png", dpi=1000)
plt.show()

df_sats_in_view_sorted = df.sort_values('sats_in_view')

df_sats_in_view_sorted['cumulative_count'] = df_sats_in_view_sorted.groupby('sats_in_view').cumcount() + 1  # Cumulative count per unique value
print(df_sats_in_view_sorted['cumulative_count'])
print(df_sats_in_view_sorted['sats_in_view'].count())
df_sats_in_view_sorted['cdfsats_in_view'] = df_sats_in_view_sorted['cumulative_count'] / df_sats_in_view_sorted['sats_in_view'].count()  # Divide by total number of observations
print(df_sats_in_view_sorted['cdfsats_in_view'].count())

print(df_sats_in_view_sorted)

plt.step(df_sats_in_view_sorted['sats_in_view'], df_sats_in_view_sorted['cdfsats_in_view'], where='post')
#plt.plot(df['SATS'], df['cdf'])
plt.xlabel('sats_in_view')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function')
plt.savefig("CDFsats_in_view.png", dpi=1000)
plt.show()
