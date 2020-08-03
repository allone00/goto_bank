"""
Добро пожаловать в АБС всея GoTo!
"""
import time
# import json


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
    ][mark-1]


def table(money, mark, p, hour):
    percent = money * interate(mark)
    payout = p - percent
    money -= payout
    penny = pennyrate(mark) * p * hour
    return [percent, payout, money, penny]  # todo: В каком формате отправлять таблицу?


def _f(money, hours, mark):  # todo: убрать после поправок ставок
    print(f"interate = {money * ((interate(mark) + 1) ** (hours // 4)) - money},\n"
          f"pennyrate = {money * pennyrate(mark)}.")
    return None

while True:
    print("test")
    time.sleep(100)
