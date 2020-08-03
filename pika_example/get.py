import pika  # pip install pika

# Подключение к брокеру сообщений
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Подключение к каналу
channel.queue_declare(queue='test')

# Функция, которая обрабатывает все запросы
def callback(ch, method, properties, body):  # Скоро опишу
    print(body)

channel.basic_consume(on_message_callback=callback, queue='test', auto_ack=False)

# Начать прослушивание канала
channel.start_consuming()
# Для того, что бы закончить программу, надо нажать CTRL + C


# Чуть позже я полностью опишу как работать с rmq
