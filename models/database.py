from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///example.db')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=engine))
Base = declarative_base()
Base.query = session.query_property()

if __name__ == '__main__':
    import models.models
    Base.metadata.create_all(bind=engine)