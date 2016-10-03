# -*- coding:utf-8 -*-

import logging


DEBUG = True
Security = True # xsrf_cookies

LOG_POSITION = './log/log.log'
LOG_FORMAT = '[%(asctime)s] %(name)s %(levelname)-8s %(message)s'
LOG_LEVAL = logging.INFO

MYSQL_DB_LINK = 'mysql+pymysql://tornado:tornado@192.168.1.108/tornadodemo'