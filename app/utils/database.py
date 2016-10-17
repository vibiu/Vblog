import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Session = sessionmaker()


class DB():
    def __init__(self, engine):
        self.engine = create_engine(engine)
        self.Model = declarative_base(bind=self.engine)
        self.session = Session(bind=self.engine)
        self.Integer = sqlalchemy.Integer
        self.String = sqlalchemy.String
        self.Unicode = sqlalchemy.Unicode
        self.Column = sqlalchemy.Column
        self.DateTime = sqlalchemy.DateTime

    def create_all(self):
        self.Model.metadata.create_all()

    def drop_all(self):
        self.Model.metadata.drop_all()

db = DB('sqlite:///blog.db')
