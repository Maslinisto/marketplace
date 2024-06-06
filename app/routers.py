from fastapi import APIRouter
from app.database import Author, Book
from app.db_operations import session

router=APIRouter(
    prefix='/test',
    tags=['Тест']
)

@router.get("/")
def read_root():
    return (session.query(Author).all())

@router.get("/items")
def read_item():
    new_book = Book(title='New Book Title', copyright=2024, author_id=1)
    session.add(new_book)
    session.commit()
    return new_book
