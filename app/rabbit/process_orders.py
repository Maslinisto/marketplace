import json
from app.rabbit.rabbitmq import RabbitMQ
from app.database import SessionLocal
from app.models.orders import Orders

def process_order(ch, method, properties, body):
    db = SessionLocal()
    order_data = json.loads(body)
    
    try:
        # Подтверждение заказа
        order = db.query(Orders).filter(Orders.order_id == order_data["order_id"]).first()
        if not order:
            raise ValueError("Order not found")
        
        order.status = "Подтвержден"
        db.commit()
        
        # Обновление статуса заказа
        order.status = "В процессе"
        db.commit()
        
        # Публикация сообщения в очередь уведомлений
        notification_message = json.dumps({
            "user_id": order_data["user_id"],
            "order_id": order_data["order_id"],
            "status": "Ваш заказ подтвержден и готовится к доставке"
        })
        print('1 работаем в new_orders, получили инфу:', notification_message)
        rabbitmq = RabbitMQ(host='localhost')
        rabbitmq.publish_message('notify_customers', notification_message)
        rabbitmq.close_connection()
        
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        db.rollback()
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
    finally:
        db.close()

def run():
    rabbitmq = RabbitMQ(host='localhost')
    rabbitmq.consume_messages('new_orders', process_order)
