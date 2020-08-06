import pika  # Не забудьте добавить зависимости в requirements.txt
import json

# Подключение к брокеру сообщений
channel = pika.BlockingConnection(pika.ConnectionParameters(
    "rmq", 5672, "/", pika.PlainCredentials("rabbitmq", "rabbitmq"))).channel()

# Подключение к каналу
channel.queue_declare(queue='test')  # Писать свой канал


# Функция, которая обрабатывает все запросы
def callback(a, b, c, body):  # Тело запроса (json) находится в body
    ans = json.loads(body)  # Json - строка  =>  Python объект (словарь)
    print(ans)


channel.basic_consume(on_message_callback=callback, queue='test', auto_ack=False)

# Начать прослушивание канала
channel.start_consuming()
# Для того, что бы закончить программу, надо нажать CTRL + C
