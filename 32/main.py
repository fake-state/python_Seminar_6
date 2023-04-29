# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

quantity = int(input('Введите количество элементов в массиве > '))
min_range = int(input('Диапазон чисел от > '))
max_range = int(input('До > '))

list = []
for i in range(quantity):
    list.append(randint(1, 1000))

list_of_index = []
for i in range(len(list)):
    if list[i] > min_range and list[i] < max_range:
        list_of_index.append(i)
print(list)
print(list_of_index)
