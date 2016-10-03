# -*- coding: utf-8 -*-

from .base import *
from .auth import *

# 暂时如此
def init_db():
    Base.metadata.create_all(engine)

init_db()
