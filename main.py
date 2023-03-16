from fastapi import FastAPI
from models import Article
from config import engine
import models
from schemas import ArticleSchema
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
async def index():
    return {'message': 'Hello World!'}


# @app.get('/acticles/{id}')
# async def get_article(id: int):
#     return {'article': id}
#
#
# @app.post('/article/')
# async def add_article(article: Article):
#     return article


# https://www.youtube.com/watch?v=d_ugoWsvGLI
def get_article(db: Session, skip: int=0, limit: int=100):
    return db.query(Article).offset(skip).limit(limit).all()

def get_article_by_id(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def create_article(db: Session, article: ArticleSchema):
    _article = Article(title=article.title, description=article.description)
    db.add(_article)
    db.commit()
    db.refresh(_article)

    return _article
