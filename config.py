from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# TODO: создать новую ДБ?
DATABASE_URL = 'postgresql://home:123456@localhost/articles'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, authflush=False, bind=engine)
Base = declarative_base(bind=engine)

