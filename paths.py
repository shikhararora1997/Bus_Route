import pandas as pd
from datetime import datetime

def getname(num,stopnames): #Helper function to get the name of the stop from stop_id
    for x in stopnames.itertuples():
        if int(x[1])==int(num):
            return x[3]

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
                          

def directpath(srcid,destid):
    stoptimes=pd.read_csv('/Users/shikhararora/Desktop/IIITD_app/static/stop_times.txt')
    route=pd.read_csv('/Users/shikhararora/Desktop/IIITD_app/static/routes.txt')
    stopnames=pd.read_csv('/Users/shikhararora/Desktop/IIITD_app/static/stops.txt')
    trips=pd.read_csv('/Users/shikhararora/Desktop/IIITD_app/static/trips.txt')
    routes={}  # dict to store all routes
    idx=0
    #[2] >str(datetime.now().time()
    for x in stoptimes.itertuples():
        if x[4]==int(srcid):  #comparing with the current time to check whether route is possible
            idx=x[0]
            stops=[]
            t=x[1]
          
            while stoptimes.loc[idx]['trip_id']==t and int(stoptimes.loc[idx]['stop_id'])!=int(destid):
                
                x=dict()
                x.update({getname(stoptimes.loc[idx]['stop_id'],stopnames):stoptimes.loc[idx]['arrival_time']})
                stops.append(x)
                idx=idx+1
            stops.append(stoptimes.loc[idx]['stop_id'])

            if len(stops)>0 and str(stops[-1])==str(destid):   #only if the destination stop matches with the last stop in stop dict, then add it to dict object
    
                stops.pop()
                last=dict()
                last.update({getname(destid,stopnames):stoptimes.loc[idx]['arrival_time']})
                stops.append(last)
                routes.update({getbusname(t,trips,route):stops})
    return routes           


