from fastapi import FastAPI
from models import Article
from config import engine
import models
from router import router
from schemas import ArticleSchema
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/index')
async def index():
    return {'message': 'Welcome Home!'}


app.include_router(router, prefix='article', tags=['article'])

# @app.get('/acticles/{id}')
# async def get_article(id: int):
#     return {'article': id}
#
#
# @app.post('/article/')
# async def add_article(article: Article):
#     return article

