from fastapi import APIRouter
from app.database import Author
from app.db_operations import session

router=APIRouter(
    prefix='/test',
    tags=['Тест']
)

@router.get("/")
def read_root():
    return (session.query(Author).all())

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
