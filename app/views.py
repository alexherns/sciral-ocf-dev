# -*- coding: utf-8 -*-
from app import app, db, models
from flask import render_template, flash, redirect, session, url_for, request
from .forms import searchBox
from .models import Article
from .scripts import fetch_articles, query_local_database
import json, urllib2
from config import ALTMETRIC_KEY

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form= searchBox()
    if form.validate_on_submit():
            flash('Search for {0} was successfully accepted!'.format(form.query_term.data))
            #session['query_term']= form.query_term.data
            return redirect(url_for('search', query_term=form.query_term.data))
    return render_template('index.html', title='', form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    default_option= request.args['default_option']
    form= searchBox()
    if default_option == 'True':
        articles= models.Article.query.filter(models.Article.default_set == True).order_by(models.Article.score.desc()).all()
    else:
        #articles= models.Article.query.filter(models.Article.default_set == False).order_by(models.Article.score.desc()).all()
        articles= request.args['articles']
    if form.validate_on_submit():
            flash('Search for {0} was successfully accepted!'.format(form.query_term.data))
            return redirect(url_for('search', query_term=form.query_term.data))
    return render_template('results.html', title='', form=form, articles=articles)

@app.route('/search', methods=['GET', 'POST'])
def search():
    query_term= request.args['query_term']
    """try:
        response= urllib2.urlopen('http://api.altmetric.com/v1/citations/1w?q={0}&key={1}'.format(query_term, ALTMETRIC_KEY))
    except urllib2.HTTPError:
        flash('No results were obtained for your query. Returning a default set.'.format(query_term))
        default_option= True
        return redirect(url_for('results', default_option=default_option))
    default_option= False
    data= json.load(response)
    articles= fetch_articles(data)
    form= searchBox()
    old_articles= models.Article.query.filter(models.Article.default_set == False).all()
    for a in old_articles:
        db.session.delete(a)
    for article in articles:
        db.session.add(article)
    db.session.commit()"""
    articles= query_local_database(query)
    if len(articles) == 0:
        flash('No results were obtained for your query. Returning a default set.'.format(query_term))
        default_option= True
        return redirect(url_for('results', default_option=default_option))
    return redirect(url_for('results', default_option=default_option, articles=articles))
