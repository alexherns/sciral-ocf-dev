from app import db, app
import flask.ext.whooshalchemy as whooshalchemy

class Article(db.Model):
    __tablename__= 'articles'
    __searchable__= ['title', 'abstract']
    id= db.Column(db.Integer, primary_key=True) # almetric ID must be unique
    title= db.Column(db.String(1000), index=True, unique=True) # title must be provided, and be unique
    doi= db.Column(db.String(100))
    journal= db.Column(db.String(1000))
    score= db.Column(db.Integer)
    abstract= db.Column(db.String(10000))
    default_set= db.Column(db.Boolean, nullable=False)
    pub_date= db.Column(db.Integer)

    def get_id(self):
        return unicode(self.id)
        
    def is_unique(self):
        if Article.query.filter_by(title=self.title).first() is None and Article.query.filter_by(id=self.id).first() is None:
            return True
        else:
        	return False

    def __repr__(self):
        return '<Article ID: {0}, {1}>'.format(self.id, self.title)
    
    

whooshalchemy.whoosh_index(app, Article)
