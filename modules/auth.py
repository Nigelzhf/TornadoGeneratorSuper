# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, VARCHAR,ForeignKey, Float

from .base import *


class Auth(Base):
    __tablename__ = "auth"
    uuid = Column(VARCHAR(36), primary_key=True)
    username = Column(VARCHAR(32),nullable=False)
    password = Column(VARCHAR(32),nullable=False)

    def save(self):
        session.add(self)
        session.commit()
        return self

    def upgrade(self):
        session.commit()
        return self

    def delete_one(self):
        session.delete(self)
        session.commit()
        return self

    @staticmethod
    def delete_all():
        for i in session.query(Auth).filter():
            session.delete(i)
        session.commit()
