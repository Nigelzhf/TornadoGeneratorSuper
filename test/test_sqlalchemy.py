# -*- coding: utf-8 -*-

from modules import *
import uuid
from util.encryption import random_str

try:
    username = 'test'
    test = Auth(uuid='00000000-0000-0000-0000-000000000002',
                    username=username,
                    password='test')
    test.save()
except:
    print('test is in the database')

try:
    username = 'root'
    root = Auth(uuid='00000000-0000-0000-0000-000000000001', username=username,
                password='toor')
    root.save()
except:
    print('root is in the database')


# Auth.delete_all()