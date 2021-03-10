# 1. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.
#


list_surnames = []

with open("names.txt", 'r') as file:
    data = file.readlines()
    for x in data:
        list_surnames.append(x.split('\t')[1])
    print(list_surnames)
