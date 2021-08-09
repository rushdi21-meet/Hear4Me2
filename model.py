from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Volunteer(Base):
    __tablename__ = 'volunteers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    username = Column(TEXT)
    password = Column(String)

