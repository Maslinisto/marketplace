from fastapi import APIRouter
from app.models import Author, Book
from app.database import session

router=APIRouter(
    prefix='/test',
    tags=['Тест']
)

@router.get("/")
def read_root():
    return (session.query(Author).all())

@router.get("/items")
def read_item():
    new_book = Author(first_name = 'mr', last_name = 'scvs',)
    session.add(new_book)
    session.commit()
    return new_book
#query = update(Author).where(Author.id==1).values(last_name="daaaas")
#result = session.execute(query)