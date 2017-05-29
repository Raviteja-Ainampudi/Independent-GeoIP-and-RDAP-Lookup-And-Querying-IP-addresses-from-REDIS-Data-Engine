# -*- coding: utf-8 -*-
"""
Created on Tue May 02 16:34:24 2017

@author: RAVI TEJA
"""

import pandas as pd
import numpy as np
from math import isnan

df = pd.read_csv("/home/osboxes/Downloads/swimlane/GeoIPCountryWhois.csv", names = ["startip","endip","startnum","endnum","code","country"], low_memory=False)
df2 = pd.read_csv("/home/osboxes/Downloads/swimlane/GeoLiteCity-Blocks.csv", names =["startIpNum","endIpNum","locId"], low_memory=False)
df3 = pd.read_csv("/home/osboxes/Downloads/swimlane/GeoLiteCity-Location.csv", names = ["locId","country","region","city","postalcode","latitude","longitude","metrocode","areacode"], low_memory=False)
df4 = pd.read_csv("/home/osboxes/Downloads/swimlane/GeoIPASNum2.csv", names=["startnum","endnum","asn"], low_memory=False)

def func1(x):
    """This fuction calls func2(x) to determine the location ID and Start IP Number. 
    And then the paramters of GeoIP obatined by data analysis tools like Pandas and Numpy."""
    
    cnty, ind = func2(x)
    if cnty == "Not Valid GeoIP":
        return cnty
    else:
        sipnum = df.get_value(ind,"startnum")
        eipnum = df.get_value(ind,"endnum")
        
        lid = df2["locId"][df2["startIpNum"]==str(sipnum)].iloc[0]
        
        region = df3["region"][df3["locId"]==str(lid)].iloc[0]
        city = df3["city"][df3["locId"]==str(lid)].iloc[0]
        postalcode = df3["postalcode"][df3["locId"]==str(lid)].iloc[0]
        latitude = df3["latitude"][df3["locId"]==str(lid)].iloc[0]
        longitude = df3["longitude"][df3["locId"]==str(lid)].iloc[0]
        metrocode = df3["metrocode"][df3["locId"]==str(lid)].iloc[0]
        areacode = df3["areacode"][df3["locId"]==str(lid)].iloc[0]
        
        try:
            s = df4["asn"][df4["startnum"]==(sipnum)].iloc[0]
            s = s.split(" ")
            s = s[1:]
            subscriber = " ".join(s)
            
        except:
            subscriber = None
            
        temp = [cnty, region, city, postalcode, latitude, longitude, metrocode, areacode, subscriber, sipnum, eipnum, lid]
        for r in temp:
            try:
                pop = isnan(r)
                temp[temp.index(r)] ="Data not Available"
            except:
                pass
            
        cnty, region, city, postalcode, latitude, longitude, metrocode, areacode, subscriber, sipnum, eipnum, lid = temp   
        return temp

        #Can be used for Unit Testing
        """        
        print cnty, region, city, postalcode
        print latitude, longitude, metrocode, areacode        
        print subscriber
        print sipnum, eipnum, lid
        """


def func2(x):
    """ This fucntion is crictical in determing the IP address in which set it falls.
    4 level functions used accordinly to determine the Location Id and Start IP Number."""
    
    ip = map(int, x.split("."))
    for i,j in df[["startip", "endip"]].values:
        st = map(int, i.split("."))
        ed = map(int, j.split("."))
        
        def level1(a,b,c):
            if b>=a and b < c:
                return 10
            elif a==b or b==c:
                return 20
            else:
                pass
                
        def level2(a,b,c):
            if  b <c:
                return 10
            elif a==b or b==c:
                return 20
            else:
                return 0
        
        def level3(a,b,c):
            if b < c:
                return 10
            elif a==b or b==c:
                return 20
            else:
                return 0
                
        def level4(a,b,c):
            if b < c:
                return 10
            elif a==b or b==c:
                return 20
            else:
                return 0
                
        if level1(st[0],ip[0],ed[0]):
            m = np.where(df["startip"]== i)
            ind = m[0][0]
            if level1(st[0],ip[0],ed[0]) == 10:
                    return df.get_value(ind,"country"), ind
            elif level1(st[0],ip[0],ed[0]) == 20:
                    if level2(st[1],ip[1],ed[1]) == 10:
                        return df.get_value(ind,"country"), ind
                    elif level2(st[1],ip[1],ed[1]) == 20:
                        if level3(st[2],ip[2],ed[2])==10:
                            return df.get_value(ind,"country"), ind
                        elif level3(st[2],ip[2],ed[2])==20:
                            if level4(st[3],ip[3],ed[3])==10:
                                return df.get_value(ind,"country"), ind
                            elif level4(st[3],ip[3],ed[3])==20:
                                return df.get_value(ind,"country"), ind
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
            else:
                pass
                     
    return "Not Valid GeoIP", None
    
    
if __name__ == "__main__":
    #Some Available test cases and their locations
    #print func1("190.216.199.119") #Colombia
    #print func1("31.57.136.230") #Iran
    #print func1("45.218.95.161") #Morocco
    #print func1("27.22.236.35") #China
    #print func1("208.128.240.230") #USA
    #print func1("40.66.137.0") #USA
    #print func1("3.221.25.119") #USA
    #print func1("60.9.40.235") #China
    #print func1("118.170.198.148") #Taiwan
    #print func1("2.111.205.111") #Denmark
    #print func1("73.95.135.112") #USA
    #print func1("238.204.59.252") #Not Valid GeoIP as IP range is upto 223.255.255.255
    #print func1("14.225.215.166") #Vietnam
    #print func1("204.244.92.77") #Canada
    #print func1("83.86.201.252")#Netherlands
    print func1("221.58.181.228") #Japan
   
    pass
    
