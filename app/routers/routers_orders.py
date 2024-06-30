from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dao.dao_orders import OrdersDAO
from app.rabbit.rabbitmq import RabbitMQ
import json
from app.config import settings

router=APIRouter(
    prefix='/orders',
    tags=['Заказы']
)
@router.post("/create_order")
def create_order(user_id: int, db: Session = Depends(get_db)):
    try:
        order = OrdersDAO.create_order(user_id, db)
        order_message = json.dumps({
            "order_id": order.order_id,
            "user_id": user_id,
            "shipping_address": order.shipping_address,
            "payment_method": order.payment_method,
            "items": order.ordered_items
        })
        rabbitmq = RabbitMQ(host=settings.RABBITMQ_HOST)
        rabbitmq.publish_message('new_orders', order_message)
        #print('0, закинули данные в new_orders:', order_message)
        rabbitmq.close_connection()
        return {"message": "Order created successfully", "order_id": order.order_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
