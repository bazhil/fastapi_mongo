from sqlalchemy import Column, Integer, String
from config import Base

class Article(Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(400))

