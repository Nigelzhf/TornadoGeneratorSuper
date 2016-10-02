import redis

r = redis.Redis(host='192.168.1.108',port=6379,db=0)

print(r.dump("tornadsession"))
