# -*- coding: utf-8 -*-
"""
Created on Wed May 03 11:51:03 2017

@author: RAVI TEJA
"""
import requests
import json
import re


def rdaplookup(x):
    """ This function is used to obatin RDAP Lookups from an external website - http://rdap.apnic.net/ip/{address}
    HTTP requests sent for every lookup and outprint string converted to unicode using JSON. And regular expressions
    are used to parse the string to obatin desired paramters from that output chunck."""
    
    
    url = "http://rdap.apnic.net/ip/"    #Website to attain the RDAP lookup data.
    url+=str(x)
    try:
        page = requests.get(url)
        k = page.content
        json_acceptable_string = k.replace('"', "\"")
        d = json.loads(json_acceptable_string)
    except:
        d = {}
    
    try:
        handle = d["handle"]
        handle = handle.encode("ascii","ignore")
    except:
        handle = "Data not available"
        
    try:    
        ipver = d["ipVersion"]
        ipver = ipver.encode("ascii","ignore")
    except:
        ipver = "Data not available"
    
    try:
        name = d["name"]
        name = name.encode("ascii","ignore")
    except:
        name = "Data not available"
     
    try: 
        typ = d["type"]
        typ = typ.encode("ascii","ignore")
    except:
        typ = "Data not available"
        
    try:
        cnty = d["country"]
        cnty = cnty.encode("ascii","ignore")
    except:
        cnty = "Data not available"
    
    k = str(d)
    try:
        a = re.findall(u"'label':(.*?)}",k)
        address = []
        for i in a:
            j = i.replace("\\n", " ")
            address.append(j[3:-1])
        address = list(set(address))
    except:
        address = "No Data found"
        
    try:
        e = re.findall(u"'email',(.*?)]",k)
        email = []
        for i in e:
            j = i.split(" ")
            email.append(j[-1][2:-1])
        email = list(set(email))
    except:
        email = "No Data found"
    
    try:    
        p = re.findall(u"'text', (.*?)]",k)
        phone = []
        for i in p:
            if "+" in i and "-" in i:
                j = i[2:-1]
                phone.append(j)
        phone = list(set(phone))
    except:
        phone = "No Data found"
    
    temp = [handle, ipver, name, typ, cnty, email, address, phone]
    
    #print handle, ipver, name, typ, cnty, email, address, phone  #Useful while Unit testing  
    
    return temp



if __name__ == "__main__":
                #Test cases below
    #print rdaplookup("33.67.141.226")   
    #print rdaplookup("153.162.86.172")
    #print rdaplookup("65.100.100.42")
    #print rdaplookup("208.128.240.230")
    print rdaplookup("221.58.181.228")
    #print rdaplookup.__doc__
    pass

   

    
    
