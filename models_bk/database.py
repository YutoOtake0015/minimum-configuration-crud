from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///example.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

if __name__ == '__main__':
    from modelsk import *
    Base.metadata.create_all(bind=engine)