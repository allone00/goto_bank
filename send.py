import pika
import json
from app import fake_variable

credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='db')
channel.queue_declare(queue='api')
#channel.queue_declare(queue='ui')

transferring_to_db = {"function": "ncredit", "user_hash": fake_variable, "sum": 20000}

channel.basic_publish(exchange='',
                   routing_key='db',
                   body=json.dumps(transferring_to_db))

# print " [x] Sent 'Hello World!'"
connection.close()