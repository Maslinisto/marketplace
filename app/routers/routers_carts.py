# routers/cart.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dao.dao_carts import CartsDAO

router=APIRouter(
    prefix='/carts',
    tags=['Корзина']
)

@router.post("/add_to_cart")
def add_to_cart(user_id: int, product_id: int, quantity: float, db: Session = Depends(get_db)):
    try:
        CartsDAO.add_to_cart(user_id, product_id, quantity, db)
        return {"message": "Product added to cart successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
