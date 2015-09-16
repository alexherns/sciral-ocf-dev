#!flask/bin/python
import os, unittest
from app import app, db, models
from app.models import Article
from app.scripts import fetch_articles

class TestCase(unittest.TestCase):

    import urllib2, json
    response= urllib2.urlopen('http://api.altmetric.com/v1/citations/1d')
    data= json.load(response)
    global articles
    articles= fetch_articles(data)
    def test_unique(self):
        titles= []
        old_articles= models.Article.query.all()
        for old in old_articles:
            db.session.delete(old)
        db.session.commit()
        for article in articles:
                assert article.title not in titles
                titles.append(article.title)
                print article.doi, article.id, article.title, article.journal, article.score, article.abstract[:10]
                db.session.add(article)
                db.session.commit()



if __name__ == '__main__':
    unittest.main()
