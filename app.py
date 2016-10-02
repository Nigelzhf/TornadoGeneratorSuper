# -*- coding: utf-8 -*-
#
# Copyright @ 2014 Mitchell Chu

import os
import tornado.web
import tornado.httpserver
import tornado.ioloop

import config
from torndsession.sessionhandler import SessionBaseHandler
from handler.TestHandler import *


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
            (r'/test', TestHandler),
        ]
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "login_url": "/login",
            "cookie_secret": "61oETzKxqAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            "xsrf_cookies": config.Security,
            "debug": config.DEBUG,
        }
        session_settings = dict(
            driver = "redis",
            driver_settings = dict(
                host = '192.168.1.108',
                port = 6379,
                db = 0,
                max_connections = 1024,
            )
        )
        settings.update(session = session_settings)
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
