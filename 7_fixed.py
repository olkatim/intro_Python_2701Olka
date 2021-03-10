
#
#
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = "Im the string"
def my_func(my_str):
    print("***" + my_str + "***")


my_func(my_str)


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
#
set_1 = set(my_dict_1)
set_2 = set(my_dict_2)

set_3 = set_1.intersection(set_2)
print(set_3)
#
#    Б
#

set_1 = set(my_dict_1)
set_2 = set(my_dict_2)

set_3 = set_1.difference(set_2)
print(set_3)

