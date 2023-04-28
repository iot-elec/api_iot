from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import config

uri = config.Config().SQLALCHEMY_DATABASE_URI
print(uri)

engine = create_engine(uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():

    Base.metadata.create_all(bind=engine)

    print(Base)
