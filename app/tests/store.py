from jinja2 import Template
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

engine1 = create_engine('sqlite:///test1.db', echo=True)
engine2 = create_engine('sqlite:///test2.db', echo=True)
Base1 = declarative_base(bind=engine1)
Base2 = declarative_base(bind=engine2)

session1 = Session(bind=engine1)
session2 = Session(bind=engine2)


class User(Base1):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


def render_template():
    with open('index.html') as f:
        html = f.read()
        mak = Template(html)
        # out = mak.render(articles=[{'id': '1', 'title': 'hello world'}])
        out = mak.render()
        print(out)

# render_template()


def create_all():
    Base1.metadata.create_all()
    Base2.metadata.create_all()


def insert_user():
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
    # session.add(ed_user)
    # session.commit()
    session2.add(ed_user)
    session2.commit()
    print('create new use ok.')


# create_all()

insert_user()
