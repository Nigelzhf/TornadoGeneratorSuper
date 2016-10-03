# -*- coding:utf-8 -*-

import logging
import tornado
import tornado.web
from handler.BaseHandler import BaseHandler
import config
from . import signin_

logging.basicConfig(format=config.LOG_FORMAT, filename=config.LOG_POSITION, filemode='w+')
log = logging.getLogger('degug_')
log.setLevel(config.LOG_LEVAL)



class MainHandler(BaseHandler):
    # @tornado.web.authenticated
    def get(self):
        # user = tornado.escape.xhtml_escape(self.current_user)
        username = self.get_secure_cookie('username')
        print('when main' + str(self.session.session))
        is_signed = self.get_secure_cookie('id')
        self.render("index.html", option={'username':username, 'is_signed':is_signed})


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        print('befor login:' + str(self.session.session))
        # uid = str(uuid.uuid1())
        username = self.get_argument('username')
        password = self.get_argument('password')

        is_signin, uid = signin_(username, password)    #xss

        if not (is_signin):
            self.redirect('/login')

        self.session.session = {
            'username': username,
            'id': uid,
            'version': '0.0.0',
            'option': {
                'a': 1,
                'b': 2,
                'c': 3,
            }
        }
        print('after login:' + str(self.session.session))
        self.set_secure_cookie("username", username)
        self.set_secure_cookie("id", uid)
        self.redirect('/')


class LogoutHandler(BaseHandler):

    def get(self):
        uid = self.get_current_user()
        self.session.session = {}
        self.clear_all_cookies()
        self.redirect("/login")

    def post(self):
        uid = self.get_current_user()
        self.session.session = {}
        self.clear_all_cookies()
        self.redirect("/login")


if config.DEBUG:
    class TestHandler(BaseHandler):
        def get(self):
            self.session["a"]='a'
else:
    class TestHandler(BaseHandler):
        def get(self):
            self.write("")
