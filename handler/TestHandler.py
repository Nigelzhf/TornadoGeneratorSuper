# -*- coding:utf-8 -*-

from handler.BaseHandler import *


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        user = tornado.escape.xhtml_escape(self.current_user)
        self.render("index.html", user=user)


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        self.set_secure_cookie("user", self.get_argument("username"))
        self.redirect("/")


class LogoutHandler(BaseHandler):
    def post(self):
        self.set_secure_cookie("user", "")
        self.redirect("/")