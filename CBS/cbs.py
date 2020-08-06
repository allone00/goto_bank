"""
Добро пожаловать в АБС всея GoTo!
"""
import json
import pika


def interate(mark: int):  # todo: подправить ставки
    """
    Возвращает ставку по кредиту
    """
    return [
        0.256,
        0.123,
        0.0999,
        0.0777,
        0.069,
        0.054,
        0.04,
        0.0333,
        0.0256,
        0.0123
    ][mark - 1]


def pennyrate(mark: int):  # todo: поправить ставки
    """
    Возвращает ставку по неуплате
    """
    return [
        1.024,
        0.64,
        0.512,
        0.4,
        0.32,
        0.256,
        0.2,
        0.16,
        0.128,
        0.08
    ][mark - 1]


def table(money, rate, penny, start, days, transactions):  # todo: Как получать транкзации
    p = money * (rate + (rate / ((rate + 1) ** days - 1)))
    s = [["Оплата", "Часов неуплачено", "Общий долг", "Реальный платёж", "Платёж в день",
          "Уплачено погашение процентов", "Просрочка погашение процентов", "Погашение процентов",
          "Уплачено погашение долга", "Просрочка погашения долга", "Погашение долга", "Уплачено пенни",
          "Просрочка пенни", "Пенни", "Уплачено пользование ОД", "Просрочка пользование ОД", "Пользование ОД",
          "Переплата"]]
    for day in range(1, days + 1):
        hours = [0, 0, 0, 0, 0, 12, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0][day]
        ss = [None for _ in range(18)]
        ss[3] = [p, p, p, p, p, 0, 1000000, p, p, p, p, p, p, p, p, p, p, p, p][day]
        ss[0] = day
        ss[1] = hours
        if day == 1:
            ss[2] = money
        else:
            ss[2] = s[day - 1][2] - s[day - 1][8]
        if day == days:
            ss[4] = ss[2] * (1 + rate)
            ss[3] = ss[4]
        else:
            ss[4] = p
        ss[7] = ss[2] * rate
        if day == 1:
            ss[5] = min(ss[3], ss[7])
        else:
            ss[5] = min(ss[3], ss[7] + s[day - 1][6])
        if day == 1:
            ss[6] = ss[7] - ss[5]
        else:
            ss[6] = ss[7] - ss[5] + s[day - 1][6]
        ss[10] = ss[4] - ss[7]
        if day == 1:
            ss[8] = min(ss[3] - ss[5], ss[10])
        else:
            ss[8] = min(ss[3] - ss[5], ss[10] + s[day - 1][9])
        if day == 1:
            ss[9] = ss[10] - ss[8]
        else:
            ss[9] = ss[10] - ss[8] + s[day - 1][9]
        ss[13] = (ss[6] + ss[9]) * penny
        if day == 1:
            ss[11] = min(ss[3] - ss[5] - ss[8], ss[13])
        else:
            ss[11] = min(ss[3] - ss[5] - ss[8], ss[13] + s[day - 1][12])
        if day == 1:
            ss[12] = ss[13] - ss[11]
        else:
            ss[12] = ss[13] - ss[11] + s[day - 1][12]
        if ss[1] == 0:
            ss[16] = 0
        else:
            ss[16] = ss[2] * rate / 12 * ss[1]
        if day == 1:
            ss[14] = min(ss[3] - ss[5] - ss[8] - ss[11], ss[16])
        else:
            ss[14] = min(ss[3] - ss[5] - ss[8] - ss[11], ss[16] + s[day - 1][15])
        if day == 1:
            ss[15] = ss[16] - ss[14]
        else:
            ss[15] = ss[16] - ss[14] + s[day - 1][15]
        ss[17] = ss[3] - ss[5] - ss[8] - ss[11] - ss[14]
        s.append(ss)
    return s


def _f(money, hours, mark):  # todo: убрать после поправок ставок
    print(f"interate = {money * ((interate(mark) + 1) ** (hours // 4)) - money},\n"
          f"pennyrate = {money * pennyrate(mark)}.")
    return None


def send(queue, ans):
    body = json.dumps(ans)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        "rmq", 5672, "/", pika.PlainCredentials("rabbitmq", "rabbitmq")))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='', routing_key=queue, body=body)
    connection.close()


def callback(a, b, c, body):
    body = json.loads(body)
    print(body)


if __name__ == "__main__":
    channel = pika.BlockingConnection(pika.ConnectionParameters(
        "rmq", 5672, "/", pika.PlainCredentials("rabbitmq", "rabbitmq"))).channel()
    channel.queue_declare(queue='cbs')
    channel.basic_consume(on_message_callback=callback, queue='cbs', auto_ack=False)
    channel.start_consuming()
