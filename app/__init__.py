import tornado
from app import view


def make_app(config):
    return tornado.web.Application([
        (r'/', view.MainHandler),
        (r'/article/(\d+)', view.ArticleHandler),
        (r'/categories', tornado.web.RedirectHandler, {'url': '/'}),
        (r'/pages', tornado.web.RedirectHandler, {'url': '/'}),
        (r'/tags', tornado.web.RedirectHandler, {'url': '/'}),
        (r'/archive', tornado.web.RedirectHandler, {'url': '/'})
    ], **config)
