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
#ploting the DataFrame
#fig = plt.figure()
#timer = fig.canvas.new_timer(interval = 15000) #creating a timer object and setting an interval of 3000 milliseconds
#timer.add_callback(close_event)

fig, ax = plt.subplots()
ax.plot(df.index, df['SATS'], label='sats_locked')
ax.plot(df.index, df['signal'], label='GPS_signal')
ax.plot(df.index, df['gsm_csq'], label='gsm_csq')
ax.plot(df.index, df['sats_in_view'], label='sats_in_view')
ax.set_xlabel('Measurement Point (based on Sampling Rate)')  # Add an x-label to the axes.
ax.set_ylabel('GPS features')  # Add a y-label to the axes.
ax.set_title("Understanding GPS")  # Add a title to the axes.
ax.legend(bbox_to_anchor=(1.30, 1.11),loc='upper right')  # Add a legend
plt.grid(True)
plt.tight_layout()
plt.savefig("GPSValues.png", dpi=1000)
plt.show()
