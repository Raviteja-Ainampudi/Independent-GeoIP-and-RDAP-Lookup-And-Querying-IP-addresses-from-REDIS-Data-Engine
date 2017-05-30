# -*- coding: utf-8 -*-
"""
Created on Tue May 02 14:46:20 2017

@author: RAVI TEJA
"""
import sys
#sys.path.insert(0,"/home/ravi/Downloads/swimlane/")  #If directory at different locataion than regular Python bin
                                                          #If expected to import other source files
import geip
import rdap
import filtering_ds

   
class lookup:
    """This class used for all IP address lookups to be parsed as data-stored in a dictionary."""
    
    import redis
    pol1 = redis.ConnectionPool(host='localhost', decode_responses=True, port=6379, db=0)
    gdb =redis.StrictRedis(connection_pool=pol1)
    pol2 = redis.ConnectionPool(host='localhost',decode_responses=True, port=6379, db=1)
    rdb = redis.StrictRedis(connection_pool=pol2)

    def __init__(self,x):
	self.gdb.set(x, geip.func1(x))
	#print geip.func1(x)
	self.rdb.set(x, rdap.rdaplookup(x))
	#print rdap.rdaplookup(x)
	
 
       
def geofilter():
    """ This function subordinates the GeoIP query, by determining the filter paramters and their associated search values."""
    
    trigger = ["cnty", "rgn", "city", "pos", "lat", "lon", "met", "area", "sub", "snum", "enum", "lid"]
    print "Parameters available for every IP address are - Country(cnty), Region(rgn), City(city), Postal Code(pos), Latitude(lat), Longitude(lon), Metro Code(met), Area Code(area), Subscriber(sub), StartIP Num(snum), EndIP Num(enum), Location ID(lid) \n"
    p1 = int(raw_input("Enter number of filters to be applied:") )   
    if p1 >0 and p1<13:
        i1 =0
        lis = {}
        while i1!= p1:
            j = raw_input("FilterApplied ChoosenName - ")
            j = j.split(" ")
            if j[0] in lis or j[0] not in trigger:
                print "This filter either already chosen or desn't exist"
            else:
                lis[j[0]] = j[1]
                i1+=1
                
        filtered_response = filtering_ds.geoquery(lookup.gdb,lis)
        if type(filtered_response) is str:
            return filtered_response
        else:
            return "The list of filtered output is: %s" %(filtered_response)
        
    else:
        print "Wrong Choice"
        geofilter()


def rdapfilter():
    """ This function subordinates the RDAP Query, by determining the filter parameters and their corresponding search values. """
    
    trigger = ["handle", "ipver", "name", "typ", "cnty", "email", "address", "phone"]
    print "Parameters available for every IP address are - Handle(handle), IPversion(ipver), Name(name), Type(typ), Country(cnty), List of Emails(email), List of Addresses(address), List of Phones(phone)) \n"
    p1 = int(raw_input("Enter number of filters to be applied:")) 
    if p1 >0 and p1<9:
        lis = {}
        i1 = 0
        while i1!=p1:
            j = raw_input("FilterApplied ChoosenName - ")
            j = j.split(" ")
            if j[0] in lis or j[0] not in trigger:
                print "This filter either already chosen or doesn't exist"
                
            else:
                lis[j[0]] = j[1]
                i1+=1
                
        filtered_response = filtering_ds.rdapquery(lookup.rdb,lis)
        if type(filtered_response) is str:
            return filtered_response
        else:
            return "The list of filtered output is: %s" %(filtered_response)
        
    else:
        print "Wrong Choice"
        rdapfilter()

    

     
if __name__ == "__main__" :
    """ IP Address extraction from random styled text document is done here."""
    
    with open("/home/ravi/Downloads/swimlane/list_of_ips (1).txt","r") as f:
        x = f.read()
        x = x.split()
        y = map(lambda s:s.strip(),x)
        #print y
    ips = {}
    for i in y:
        if i.count(".")== 3 or i.count(".")==4:
            if i.count(".")==4:
                i = i[:-1]
            a1 = i.split(".")
            a11 = []
            for k in a1:
                if "," in k:
                     k = k[:-1]
                a11.append(k)
            a1 = a11
            try:
                a2 = [int(j) for j in a1]
                a3 = [j for j in a2 if j >=0 if j <=255]
                if len(a3)==4:    
                    if i in ips:
                        ips[i]+=1
                    else:
                        ips[i]=1
                else:
                    pass
            except:
                 pass
        else:
             pass
    
    print "The total number of IP addresses extracted from the provided text file are: %s" %(len(ips))
    
    
    pool = list(ips)       #For testing used 20 IP addresses.
    for i in range(1):  # Or use "for i in range(len(pool)):"
        lookup(pool[i])
    
    print ("\n")
    if (raw_input("Want to apply filters to GeoIP lookups ? Then type YES - ")).lower()=="yes":
        print "\n"        
        print geofilter()
    else:
        pass
    
    print "\n"
    if (raw_input("Want to apply filters to RDAP lookups ? Then type YES - ")).lower()=="yes":
       print "\n"
       print rdapfilter()
    else:
        pass

