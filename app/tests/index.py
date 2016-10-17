import tornado.ioloop
from view.hello import HelloHandler
from tests.asyn import synchronous_fetch
from tests.asyn import asynchronous_fetch


def make_app():
    return tornado.web.Application([
        (r"/", HelloHandler),
    ])


def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


def test():
    # body = synchronous_fetch('http://www.ncuhome.cn')
    # print(type(body))
    # print(body.decode('utf-8'))
    def print_body(body):
        print(body.decode('utf-8'))
        print('hello world')

    asynchronous_fetch('http://www.ncuhome.cn', print_body)
    while True:
        # print('1', end="")
        pass


if __name__ == "__main__":
    test()
    # main()
