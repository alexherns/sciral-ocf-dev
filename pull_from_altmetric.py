#!flask/bin/python
from app import db, models
from config import ALTMETRIC_KEY
import urllib2, json
from app.scripts import fetch_articles

max_pages= 100

old_defaults= models.Article.query.filter(models.Article.default_set == False).all()
for a in old_defaults:
    db.session.delete(a)
db.session.commit()

for i in range(max_pages+1)[1:]:
	try:
		response= urllib2.urlopen('http://api.altmetric.com/v1/citations/1m?num_results=100&page={0}&key={1}'.format(i, ALTMETRIC_KEY))
		data= json.load(response)
		articles= fetch_articles(data)
		for article in articles:
			if article.is_unique():
				db.session.add(article)
		db.session.commit()
	except urllib2.HTTPError:
		print "HTTPError: Query term not found. Database not modified. Aborting..."
		db.session.rollback()
		db.session.commit()
		exit()
