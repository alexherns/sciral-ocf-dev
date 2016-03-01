from app import models
def fetch_articles(data):
    articles= load_altmetric_data(data)
    return articles
    # article must have almetric ID and title. Other fields are optional, but will be retrieved if possible
    articles= fetch_from_pubmed(articles)

def query_local_database(query):
    return sorted(models.Article.query.whoosh_search(query).order_by(models.Article.score.desc()).all(), key=lambda x: x.score)[::-1]

def load_altmetric_data(data):
    articles= []
    for result in data['results']:
        if 'altmetric_id' in result:
            id= result['altmetric_id']
        else:
            continue
        if 'title' in result:
            title= (result['title'].encode('ascii', errors='ignore'))
        else:
            continue
        if 'doi' not in result or 'abstract' not in result:
            continue
        doi= (result['doi'] if 'doi' in result else '')
        journal= (result['journal'] if 'journal' in result else '')
        score= (int(result['score'])+1 if 'score' in result else 0)
        abstract= (result['abstract'].encode('ascii', errors='ignore') if 'abstract' in result else '')
        pub_date= (int(result['published_on']) if 'published_on' in result else 0)
        article= models.Article(id=id, title=title, doi=doi, journal=journal, score=score, abstract=abstract, default_set=False)
        if article.is_unique():
        	articles.append(article)
    return articles

def fetch_from_pubmed(articles):
    import urllib2, fuzzywuzzy
    import xml.etree.ElementTree as ET
    data= urllib2.urlopen('http://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?tool=my_tool&email=my_email@example.com&ids=10.1093/nar/gks1195')
    tree = ET.parse(data)
    root= tree.getroot()
    if root.attrib['status'] == 'ok': # successfully found the entry on pubmed
        print root
