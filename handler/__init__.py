
from modules import *

def signin_(username='', password=''):
    auth = session.query(Auth).filter_by(username=username, password=password).first()
    if auth:
        if auth.username == username and auth.password==password:
            return (True,auth.uuid)
    else:
        return (False, '')
