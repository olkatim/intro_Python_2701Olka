# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100. Задание можно
# выполнить и через обычный цикл и через генератор списков.

import random

my_list = [random.randint(1, 100) for i in range(20)]
print(my_list)
#
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
import random

triangle = {"A": {"x": random.randint(-10, 10),
                  "y": random.randint(-10, 10)},

            "B": {"x": random.randint(-10, 10),
                  "y": random.randint(-10, 10)},

            "C": {"x": random.randint(-10, 10),
                  "y": random.randint(-10, 10)}
            }
print(triangle)

#
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = "I'm the string"
func_my_print = print("***"+my_str+"***")

##################################################################################################################

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# #
persons = [
           {"name": "John", "age": 15},
           {"name": "Tom", "age": 18},
           {"name": "Ann", "age": 24},
           {"name": "Steeve", "age": 24},
           {"name": "Jack", "age": 15}
          ]

names_ages = [(person["name"], person["age"]) for person in persons]
print(names_ages)

list_ages = []
list_names = []
for person in persons:
    list_ages.append(person["age"])
    list_names.append(person["name"])

min_age = float('inf')  # можно 0
max_len = float('-inf')  # можно 1000

for person in persons:
    if person['age'] < min_age:
        min_age = person['age']
    if len(person['name']) > max_len:
        max_len = len(person['name'])
names_min_age = [p['name'] for p in persons if p['age'] == min_age]
names_max_len = [p['name'] for p in persons if len(p['name']) == max_len]


average_sum = sum(list_ages) / len(list_ages)

print(names_min_age)
print(names_max_len)
print(average_sum)



############################################################################################################

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},


my_dict_1 = {"name": "Nick",
             "surname": "Stone",
             "phone": "+38050123456",
             "age": 35}

my_dict_2 = {"name": "Andrew",
             "surname": "Smith",
             "town": "NY",
             "age": 40}


#    A


my_list = []

for k1 in my_dict_1:
    for k2 in my_dict_2:
        if k1 == k2:
            my_list.append(k1)
print(my_list)

#    Б


my_list = []
for k in my_dict_1:
    if k not in my_dict_2:
        my_list.append(k)

print(my_list)

#   В

my_dict_3 = dict(item for item in my_dict_1.items() if item[0] not in my_dict_2)

print(my_dict_3)


# Г

my_dict_3 = dict()
for item in my_dict_1.items():
    if item[0] not in my_dict_2:
        my_dict_3[item[0]] = item[1]
    else:
        my_dict_3[item[0]] = [item[1], my_dict_2[item[0]]]

print(my_dict_3)

