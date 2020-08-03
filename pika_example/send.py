import pika  # pip install pika
import json


def send(  # Отправка сообщений
        queue,  # Канал (кому надо отправить)
        ans  # Информация (что надо отправить)
):
    body = json.dumps(ans)

    # Подключение к брокеру сообщений
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        "rmq", 5672, "/", pika.PlainCredentials("rabbitmq", "rabbitmq")))
    channel = connection.channel()

    # Подключению к каналу
    channel.queue_declare(queue=queue)

    # Отправка сообщения
    channel.basic_publish(exchange='',  # Точка обмена
                          routing_key=queue,  # Имя очереди
                          body=body)  # Текст очереди (позже использовать json)

    # Закончить отправку сообщений (Использовать только при окончании программы)
    connection.close()