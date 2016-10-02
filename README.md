# TornadoCompleteDemo

tornado
sqlalchemy+anyderiver
session 
celery
redis
完整可用的demo，不间断完善中...
[tornado session](https://github.com/mitchellchu/torndsession)
[sqlalchemy](http://www.sqlalchemy.org/)
[celery](http://docs.jinkan.org/docs/celery/)的[tornado-celery](https://github.com/mher/tornado-celery/) + Redis(tornado session用的Redis)

# 安装方法 for ubuntu

```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install virtualenv
sudo apt-get install redis

创建虚拟环境后在虚拟环境中安装requirement.txt
pip3 install -r requirements.txt
```

# session format
```
self.session.session = {'option':{}, }
```

# doc

功能基本实现，但防御比较差