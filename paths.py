import pandas as pd
from datetime import datetime
import folium
import re

def getname(num,stopnames): #Helper function to get the name of the stop from stop_id
    for x in stopnames.itertuples():
        if int(x[1])==int(num):
            return x[3],x[4],x[5]

def getbusname(t,trips,route): #Helper function to get the busname from trip_id
            routeid=-1
            for y in trips.itertuples():
                 if int(t)==int(y[3]):
                    routeid=y[1]
                    break
            if routeid!=-1:
                 for l in route.itertuples():
                    if int(routeid)==int(l[4]):
                        return l[2]

def markonmap(locations,stopsname):

    tooltip='Click for more'
    x_center=0
    y_center=0
    for x in locations:
        x_center=x_center+x[0]
        y_center=y_center+x[1]
    x_center=x_center/(len(locations))
    y_center=y_center/(len(locations))
    loc=[x_center, y_center]
    m=folium.Map(location=loc, zoom_start=16)
    idx=0
    for point in range(0, len(locations)):
        folium.Marker(locations[point],popup=str(idx+1)+'. '+str(stopsname[point])[1:-1], tooltip=str(idx+1)+'. '+str(stopsname[point])[1:-1]).add_to(m)
        idx=idx+1
    folium.PolyLine(locations, color='red', weigth=2.5, opacity=1).add_to(m)
    m.save('templates/map.html')
    return


def directpath(srcid,destid):
    stoptimes=pd.read_csv('static/stop_times.txt')
    route=pd.read_csv('static/routes.txt')
    stopnames=pd.read_csv('static/stops.txt')
    trips=pd.read_csv('static/trips.txt')
    routes={}  # dict to store all routes
    idx=0
    #[2] >str(datetime.now().time()
    for x in stoptimes.itertuples():
        if x[4]==int(srcid):  #comparing with the current time to check whether route is possible
            idx=x[0]
            stops=[]
            t=x[1]
            locs=[]
            while stoptimes.iloc[idx]['trip_id']==t and int(stoptimes.iloc[idx]['stop_id'])!=int(destid):
                
                stop=dict()
                name,x,y=getname(stoptimes.iloc[idx]['stop_id'],stopnames)
                stop.update({name:stoptimes.iloc[idx]['arrival_time']})
                stops.append(stop)
                locs.append([x,y])
                idx=idx+1
            stops.append(stoptimes.iloc[idx]['stop_id'])

            if len(stops)>0 and str(stops[-1])==str(destid):   #only if the destination stop matches with the last stop in stop dict, then add it to dict object
    
                stops.pop()
                last=dict()
                dest_name,dest_x,dest_y=getname(destid,stopnames)
                last.update({dest_name:stoptimes.iloc[idx]['arrival_time']})
                locs.append([dest_x,dest_y])
                stops.append(last)
                markonmap(locs,stops)
                routes.update({getbusname(t,trips,route):stops})
                break
    return routes           


