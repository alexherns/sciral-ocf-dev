from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class searchBox(Form):
    query_term= StringField('query_term', validators=[DataRequired()])
