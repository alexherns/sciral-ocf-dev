# -*- coding: utf8 -*-
import os, secrets
WTF_CSRF_ENABLED= True
SECRET_KEY= secrets.SECRET_KEY

# DATABASE CONFIGURATION
basedir= os.path.abspath(os.path.dirname(__file__))
if os.environ.get('DATABASE_URL') not in os.environ:
    SQLALCHEMY_DATABASE_URI = ('sqlite:///' + os.path.join(basedir, 'app.db') + '?check_same_thread=False')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True

# Setting up Whoosh-Alchemy for full-text searches
WHOOSH_BASE = os.path.join(basedir, 'search.db')

ALTMETRIC_KEY= secrets.ALTMETRIC_KEY
import os
import psycopg2
import urlparse

#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ["DATABASE_URL"])
"""
conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
                            )"""
