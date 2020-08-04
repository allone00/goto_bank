import pika

credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='db')
channel.queue_declare(queue='api')
# channel.queue_declare(queue='ui')\

# print ' [*] Waiting for messages. To exit press CTRL+C'

# def callback(ch, method, properties, body):
#     print " [x] Received %r" % (body,)

def callback(ch, method, properties, body):
    body = json.loads(body)

channel.basic_consume(on_message_callback=callback, queue='api', auto_ack=False)

# channel.basic_consume(callback,
#                       queue='api',
#                       no_ack=True)

channel.start_consuming()
