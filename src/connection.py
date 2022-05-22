from sqlalchemy import Table
from sqlalchemy.pool import NullPool
from sqlalchemy import orm, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from constants import connection

#Content Master DB Connection setup
engine = create_engine('mysql://' + connection.username + ':' + connection.password + '@' + connection.host + '/' + \
    connection.db + '?charset=utf8mb4', echo=False, pool_recycle=280, poolclass=NullPool)
meta = MetaData(bind=engine)
Session = orm.scoped_session(orm.sessionmaker(bind=engine))
Base = declarative_base()

#Model declaration
class Stationery(Base):
    __table__ = Table('stationery', meta, autoload=True)

