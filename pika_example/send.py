import pika  # pip install pika

# Подключение к брокеру сообщений
credentials = pika.PlainCredentials("rabbitmq", "rabbitmq")
parameters = pika.ConnectionParameters("rmq", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Подключению к каналу
channel.queue_declare(queue='test')

# Отправка сообщения
channel.basic_publish(exchange='',  # Точка обмена
                      routing_key='test',  # Имя очереди
                      body='Hello World!')  # Текст очереди (позже использовать json)

# Закончить отправку сообщений (Использовать только при окончании программы)
connection.close()