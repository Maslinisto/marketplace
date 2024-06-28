from app.dao.base import BaseDAO
from app.models.orders import Orders
from sqlalchemy.orm import Session
from app.models.orders import Orders
from app.models.users import Users
from app.models.carts import Carts

class OrdersDAO(BaseDAO):
    model = Orders

    @classmethod
    def create_order(cls, user_id: int, db: Session):
        user = db.query(Users).filter(Users.id == user_id).first()
        if not user:
            raise ValueError("User not found")
        
        cart_items = db.query(Carts).filter(Carts.user_id == user_id).all()
        if not cart_items:
            raise ValueError("Cart is empty")

        # Создаем новый заказ
        ordered_items = [{"product_id": item.product_id, "quantity": float(item.quantity)} for item in cart_items]
        total_amount = sum(item.cost_of_position for item in cart_items)
        
        new_order = Orders(
            user_id=user_id,
            ordered_items=ordered_items,
            total_amount=total_amount,
            shipping_address=user.shipping_address, 
            payment_method="по карте",
            shipping_method="aviasales"
        )
        
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        
        # Очищаем корзину после создания заказа
        db.query(Carts).filter(Carts.user_id == user_id).delete()
        db.commit()
        
        return new_order