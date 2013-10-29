# coding: UTF-8

from sqlalchemy.orm import Session, sessionmaker
from ..models import engine

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()