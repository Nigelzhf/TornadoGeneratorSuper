# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey, Float
from sqlalchemy.orm import relationship, backref, scoped_session, sessionmaker

import config

Base = declarative_base() #create Base lei
engine = create_engine(config.MYSQL_DB_LINK,
                       encoding='utf-8',
                       echo=True,
                       pool_size=100,
                       pool_recycle=10)

__Session = sessionmaker(bind=engine)
session = __Session()
