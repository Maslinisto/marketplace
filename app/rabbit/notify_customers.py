import json
from app.rabbit.rabbitmq import RabbitMQ
from app.config import settings


def notify_customer(ch, method, properties, body):
    notification_data = json.loads(body)
    user_id = notification_data["user_id"]
    order_id = notification_data["order_id"]
    status = notification_data["status"]
    #print('2)в 1 закинули инфу в notify: ', notification_data)
    print(f"Sending notification to user {user_id} about order {order_id}: {status}")
    # ---
    # Логика отправки уведомления
    # ---
    ch.basic_ack(delivery_tag=method.delivery_tag)

def run():
    rabbitmq = RabbitMQ(host=settings.RABBITMQ_HOST)
    print("Starting consumer for notify_customers")
    rabbitmq.consume_messages('notify_customers', notify_customer)
