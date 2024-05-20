import pika
import json
from Application.UseCase.UpdateInventoryUseCase import UpdateInventoryUseCase
from Infrastructure.Repositories.Repository import InventoryRepository

rabbitmq_settings = {
    'host': 'localhost',
    'port': 5672,
    'credentials': pika.PlainCredentials('admin', 'adminadmin')
}

print("Conectando a rabbitMQ")
connection = pika.BlockingConnection(pika.ConnectionParameters(**rabbitmq_settings))
channel = connection.channel()
print("Conectado a RabbitMQ")

print("Analyzing if the queue rderShipped exists ")
channel.queue_declare(queue='OrderShipped', durable=True)
print("Queue OrderShipped insured")

inventory_repository = InventoryRepository()

def callback(ch, method, properties, body):
    print("Message received.")
    order = json.loads(body)
    use_case = UpdateInventoryUseCase(inventory_repository)
    use_case.execute(order)
    print("processed message ")

def start_consumer():
    print("starting consumer")
    channel.basic_consume(queue='OrderShipped', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()