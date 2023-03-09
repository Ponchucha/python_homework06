# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random


def get_number_from_console(message):
    while True:
        try:
            return int(input(message))
            break
        except:
            print("Введите натуральное число")


list_len = get_number_from_console("Введите количество элементов: ")
min_num = get_number_from_console("Введите минимум: ")
max_num = get_number_from_console("Введите максимум: ")
my_list = [random.randint(-10, 10) for i in range(list_len)]
print(my_list)
result_list = []

for i in range(list_len):
    if min_num <= my_list[i] <= max_num:
        result_list.append(i)

print(result_list)
