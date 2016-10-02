# -*- coding:utf-8 -*-

import tornado.web
from torndsession.sessionhandler import SessionBaseHandler


class BaseHandler(SessionBaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")
