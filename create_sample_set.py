#!flask/bin/python
from app import db, models
from config import ALTMETRIC_KEY
import urllib2, json
from app.scripts import fetch_articles

query_term= 'genome'
try:
    response= urllib2.urlopen('http://api.altmetric.com/v1/citations/1d?q={0}&key={1}'.format(query_term, ALTMETRIC_KEY))
except urllib2.HTTPError:
    print "HTTPError: Query term not found. Database not modified. Aborting..."
    exit()

old_defaults= models.Article.query.all()
for a in old_defaults:
	db.session.delete(a)
db.session.commit()

data= json.load(response)
articles= fetch_articles(data)

for article in articles:
	article.default_set= True
	if article.is_unique():
		db.session.add(article)
db.session.commit()

