import pika
import json


def send(  # Отправка сообщений
        queue,  # Канал (кому надо отправить)
        ans  # Информация (что надо отправить)
):
    body = json.dumps(ans)  # obj -> json str

    # Подключение к брокеру сообщений
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        "rmq", 5672, "/", pika.PlainCredentials("rabbitmq", "rabbitmq")))
    channel = connection.channel()

    # Подключению к каналу
    channel.queue_declare(queue=queue)

    # Отправка сообщения
    channel.basic_publish(exchange='',  # Точка обмена (Не трогать)
                          routing_key=queue,  # Имя очереди
                          body=body)  # Текст очереди (позже использовать json)

    # Закончить отправку сообщений
    connection.close()
