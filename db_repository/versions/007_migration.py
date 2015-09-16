from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
article = Table('article', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=1000)),
    Column('doi', String(length=100)),
    Column('journal', String(length=1000)),
    Column('score', Integer),
    Column('abstract', String(length=10000)),
    Column('default_set', Boolean, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['article'].columns['default_set'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['article'].columns['default_set'].drop()
