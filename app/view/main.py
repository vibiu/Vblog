import misaka
from tornado.web import RequestHandler
from app import model
from app.utils import db


class MainHandler(RequestHandler):

    def get(self):
        articles = db.session.query(model.Article).all()
        self.render('index.html', articles=articles)


class ArticleHandler(RequestHandler):

    def get(self, id):
        article = db.session.query(model.Article) \
            .filter_by(id=id).first()
        if article:
            count = db.session.query(model.Article).count()
            body = misaka.html(article.body)
            self.render('article.html',
                        article=article, count=count, body=body)
        else:
            self.set_status(404)
            self.write('404 not found')
