import redis
pool = redis.ConnectionPool(host='localhost', decode_responses=True, port=6379, db=0)
r1 =redis.StrictRedis(connection_pool=pool)
pool2 = redis.ConnectionPool(host='localhost',decode_responses=True, port=6379, db=1)
r2 = redis.StrictRedis(connection_pool=pool2)
r1.set('foo', 'barr')
r2.set('name','ravi')
r2.set('name1','raviteja')
r2.set('name2','raviteja')
r2.set('name3','raviteja')
r2.set('name4','raviteja')
r2.set("job","SE1")
"""
print r1.get('foo')
print r2.get('name')
print r1.get('name')
print r2.get("job")
print r2.keys("*")
for i in r2.keys("*"):
	type = r2.type(i)
	print r2.get(i)
"""
print r2.keys(pattern="nam*")
print r2.smembers("name")
