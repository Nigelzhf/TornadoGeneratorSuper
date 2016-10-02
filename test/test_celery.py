# -*- coding:utf-8 -*-
from time import sleep
from celery import Celery

backend = 'redis://192.168.1.108:6379/0'
broker = 'redis://192.168.1.108/1'

app = Celery('tasks', backend=backend, broker=broker)

@app.task
def add(x, y):
    sleep(3)
    return x + y
