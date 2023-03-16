from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from config import Base

class Article(Base):
    __tablename__ = 'articles'

    id: Column(Integer, primary_key=True)
    title: Column(String)
    description: Column(String)

