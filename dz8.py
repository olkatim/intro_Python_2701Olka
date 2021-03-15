# ДЗ:
# 1. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.
#
import random
import string


def create_random_str():
    min_limit = random.randint(0, 19)
    max_limit = random.randint(20, 40)
    alpabet = string.ascii_lowercase
    rand_str = [random.choice(alpabet) for _ in range(min_limit,max_limit)]
    return "".join(rand_str)


print(create_random_str())


#####################################################################################################
#
# 2. Даны списки names и domains (создать самостоятельно).
# Написать функцию create_email для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
#
# Обязательные параметры функции: names и domains.
# Параметры по умолчанию: границы генерируемого числа (100, 999), границы генерируемой строки (5, 7)
#
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться.
#
from random import randint
import random
import string


names = ["Nick", "John", "Michel", "Steeve", "Ann"]
domains = ["net", "com", "ua", "biz"]

def create_email():
    names1 = random.choice(names)
    domains1 = random.choice(domains)
    number = random.randint(100, 999)
    alpabet = string.ascii_lowercase
    random_word = ''.join(random.choice(alpabet) for j in range(randint(5, 7)))
    email = names1 + "." + str(number) + "@" + str(random_word) + "." + domains1
    return email


print(create_email())


