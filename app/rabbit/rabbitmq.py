import pika

class RabbitMQ:
    def __init__(self, host: str):
        self.host = host
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()

    def declare_queue(self, queue_name: str):
        self.channel.queue_declare(queue=queue_name, durable=True)

    def publish_message(self, queue_name: str, message: str):
        self.channel.basic_publish(
            exchange='',
            routing_key=queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            ))

    def consume_messages(self, queue_name: str, callback):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=queue_name, on_message_callback=callback)
        self.channel.start_consuming()
    
    def close_connection(self):
        self.connection.close()

    @staticmethod
    def setup_queues(host: str, queues: list):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        channel = connection.channel()
        for queue in queues:
            channel.queue_declare(queue=queue, durable=True)
        connection.close()
