from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import ArticleSchema, RequestArticle, Response
import crud


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request: RequestArticle, db: Session=Depends(get_db)):
    crud.create_article(db, article=request.parameter)
    return Response(code=200, status='Ok', message='Article created successfully').dict(exclude_none=True)


@router.get('/')
async def get(db: Session=Depends(get_db)):
    _article = crud.get_article(db, 0, 100)
    return Response(code=200, status='Ok', message='Success fetch all data', result = _article).dict(exclude_none=True)


@router.get('/{id}')
async def get_by_id(id: int, db: Session=Depends(get_db)):
    _article = crud.get_article_by_id(db, id)
    return Response(code=200, status='Ok', message='Success get data', result=_article).dict(exclude_none=True)


@router.post('/update')
async def update_article(request: RequestArticle, db: Session = Depends(get_db)):
    article = request.parameter
    _article = crud.update_article(db, article_id=article.id, title=article.title, description=article.description)
    return Response(code=200, status='Ok', message='Successfull update article',
                    result=_article).dict(exclude_none=True)


@router.delete('/delete')
async def delete(id: int, db: Session = Depends(get_db)):
    crud.remove_article(db, article_id=id)
    return Response(code=200, status='Ok', message='Successfull delete article').dict(exclude_none=True)