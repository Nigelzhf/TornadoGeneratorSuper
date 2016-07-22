# -*- coding:utf-8 -*-

import os
import config
from handler.TestHandler import *


settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "login_url": "/login",
    "cookie_secret": "61oETzKxqAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "xsrf_cookies": config.Security,
    "debug": config.DEBUG,
}


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
], **settings)


if __name__ == "__main__":
    application.listen(config.HTTPServerPort)
    tornado.ioloop.IOLoop.instance().start()
