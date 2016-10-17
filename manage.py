import tornado.ioloop

from app import make_app
from app.utils import db
from config import config


def create():
    db.create_all()
    print('create ok!')


def main():
    app = make_app(config)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
    # create()
