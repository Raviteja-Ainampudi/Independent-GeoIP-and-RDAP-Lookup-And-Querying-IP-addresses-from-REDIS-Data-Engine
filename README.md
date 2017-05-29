# Independent-GeoIP-and-RDAP-Lookup-And-Querying-IP-addresses-from-REDIS-Data-Engine 
- Performs GeoIP and RDAP lookup of any Public IP address without internet and 3rd party packages.
- Cache mechanism is implemented through REDIS data-storage engine. 
- Model built entirely in Python.
- Data analysis by Numpy, Pandas.
- Self-learning model.
- Multiple connection-pools in Redis.
________________________________________________________________________________________________________________

1. From GeoIP lookup 12 different parameters can be obtained.
2. From RDAP lookup 8 different paramters can be obatined.
3. All the newlookups will be updated in Redis database accrodingly and queries for desired attributes can be done effectively. 
4. As the lookup databases databases used are free, the range of IP addresses this model works is 1.0.0.0 – 223.255.255.255. 
--------------------------------------------------------------------------------

* basefile.py - Central file to run the project.
* geip.py - Module which runs the GeoIP lookup
* rdap.py - Module which runs the RDAP lookup
* filtering_ds.py - Module which is used to run the queries.
* Project - Without Redis. (Conventional Dict. Storage) - Sub Folder inlcudes the same project without using the Redis data-storage.
--------------------------------------------------------------------------------

* Before you try to run the central file, please start your redis server in your machine. 
Self help available at - https://redis.io/topics/quickstart
* Please make sure redis is working alright. Resolve if any issues occured based on the errors recieved. 


