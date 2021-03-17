
# 2. Создать функцию для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.


import random
import string
import json


def random_key():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_value():
    return random.choice([random.randint(-100, 100)] or random.uniform(0, 1) or random.choice([False, True]))


def random_dict():
    return {random_key(): random_value() for _ in range(5, 20)}


def write_json_file():
    with open('data.json', 'w') as file:
        json.dump(random_dict(), file)
        print(write_json_file())


