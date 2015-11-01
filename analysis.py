import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import statsmodels.api as sm
import plot_fit as pfit
import pygmaps

number_rows=10000
#df=pd.read_csv('~/Downloads/data/trip_data_1_2010.csv', nrows=number_rows, usecols=[' pickup_longitude', ' pickup_latitude', ' dropoff_longitude', ' dropoff_latitude'])
df=pd.read_csv('~/Downloads/data/trip_data_1_2010.csv', nrows=number_rows)
#df=df[df[' pickup_latitude']!=0.0].reset_index()
rows = np.random.choice(df.index.values, 10000)
#print type(df[' pickup_latitude'][49])
#print df[' pickup_latitude'][49]
#quit()
#quit()
#print rows
#quit()
sampled_df = df.ix[rows]
#print sampled_df
#print sampled_df

#quit()


#print df.columns

#quit()
#pl.plot(df[' dropoff_longitude'], df[' dropoff_latitude'], 'ro')
#pl.plot(df[' pickup_longitude'], df[' pickup_latitude'], 'bo')
#pl.axis([-74.2, -73.65, 40.55, 40.96])
#pl.axis([-75, -73, 40, 41])
#pl.show()

#print df.columns

df_time_distance= df[[' trip_time_in_secs', ' trip_distance']]
time_sorted_df_time_distance= df_time_distance.sort_values(' trip_time_in_secs')
nbegin=int(number_rows/5.3)
#nbegin=0
time=time_sorted_df_time_distance[' trip_time_in_secs'][nbegin:]
distance= time_sorted_df_time_distance[' trip_distance'][nbegin:]
result = sm.OLS( distance, time ).fit()
fig, ax = pl.subplots()
fig = pfit.plot_fit(result, 0, ax=ax)

ax.set_ylabel("Distance")
ax.set_xlabel("Time")
#ax.set_title("Linear Regression")

#print result.summary()
#pl.plot(distance, time, 'bo')
pl.show()


#df_gps_pickup= df[[' pickup_longitude', ' pickup_latitude']]
#df_gps_dropoff= df[[' dropoff_longitude', ' dropoff_latitude']]

##name_column= pd.DataFrame('"hello"', columns=[' Column A '],  index=range(number_rows))
#new_frame=df_gps_pickup.join(name_column)

'''df_gps_pickup.to_csv("pickup.csv", cols=[' pickup_longitude', ' pickup_latitude'], index=False)
df_gps_dropoff.to_csv("dropoff.csv", cols=[' pickup_longitude', ' pickup_latitude'], index=False)'''

#print df[' pickup_longitude'][1]








################
quit()
pickup_map = pygmaps.maps(40.752928, -73.881528, 12)
dropoff_map = pygmaps.maps(40.752928, -73.881528, 12)
#mymap.setgrids(37.42, 37.43, 0.001, -122.15, -122.14, 0.001)

for i in rows:
    pickup_lat=sampled_df[' pickup_latitude'][i]

    pickup_long=sampled_df[' pickup_longitude'][i]
    dropoff_lat=sampled_df[' dropoff_latitude'][i]
    dropoff_long=sampled_df[' dropoff_longitude'][i]

    if (isinstance(pickup_lat, float) and isinstance(pickup_long, float) and isinstance(dropoff_lat, float) and isinstance(dropoff_long, float)):
        
        pickup_map.addpoint(sampled_df[' pickup_latitude'][i], sampled_df[' pickup_longitude'][i], "#FF0000")
        dropoff_map.addpoint(sampled_df[' dropoff_latitude'][i], sampled_df[' dropoff_longitude'][i], "#0000FF")
        #mymap.addradpoint(df[' pickup_latitude'][i], df[' pickup_longitude'][i], 95, "#FF0000")

pickup_map.draw('./pickup_map.html')
dropoff_map.draw('./dropoff_map.html')