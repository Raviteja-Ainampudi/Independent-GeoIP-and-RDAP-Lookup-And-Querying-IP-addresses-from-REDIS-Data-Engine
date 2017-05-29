# -*- coding: utf-8 -*-
"""
Created on Wed May 03 17:14:05 2017

@author: RAVI TEJA
"""
#For Filtering the GeoIP Lookups
def geoquery(db, lis):    
    """This function is used to filter the available 12 parameters of data from the parsed lookups for GeoIP. All 12 paramters are strings. It returns a list of desired IP address which satisfy all the filter parameters. If that list is empty, it returns a standard string"""
     
	
    trigger = ["cnty", "rgn", "city", "pos", "lat", "lon", "met", "area", "sub", "snum", "enum", "lid"]    
    filter_data = []    
    for i in db.keys("*"):
        count = 0
	temp = eval((db.get(i)).encode('latin1'))
        for k in lis:
	    if str(temp[trigger.index(k)]) == str(lis[k]):
                count +=1
        if count == len(list(lis)):
            filter_data.append(i.encode('latin1'))
        else:
            pass
    if len(filter_data)>0:
        return filter_data
    else:
        return "No data for given filters"



#For Filtering the RDAP Lookups.
def rdapquery(db, lis):
    """This fucntion is used to filetr the available 8 paramters from a parsed lookups for RDAP. The first 5 paramters are strings and next 3 paramters are list type.  It returns a list of desired IP address which satisfy all the filter parameters.
    If that list is empty, it returns a standard string."""
    
    trigger1 = ["handle","ipver","name","typ","cnty"]
    trigger2 = ["email","address","phone"]
    filter_data = []
    for i in db.keys("*"):
        count =0
	temp = eval((db.get(i)).encode('latin1'))
        for k in lis:
	    if k in trigger1:
		if str(temp[trigger1.index(k)]) == str(lis[k]):
                    count +=1
            if k in trigger2:
                if str(lis[k]) in temp[trigger2.index(k)+5]:
                    count+=1
        if count == len(list(lis)):
            filter_data.append(i.encode('latin1'))
    if len(filter_data)>0:
        return filter_data

    else:

        return "No data for given filters"  
                
            


if __name__ == "__main__":
   import basefile
   print geoquery(basefile.lookup.gdb, {"cnty":"Japan"})

   pass
