__author__ = 'Рыбка Артем Сергеевич'

import math
import random

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

def zadanie1():
    my_list = [2, -5, 8, 9, -25, 25, 4]
    new_list = list()

    for items in my_list:
        try:
            if math.sqrt(items) == int(math.sqrt(items)):
                new_list.append(math.sqrt(items))
            else:
                continue
        except:
            continue

    for items in new_list:
        print(items)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

def zadanie2():
    month = {"01": "января",
             "02": "февраля",
             "03": "марта",
             "04": "апреля",
             "05": "майя",
             "06": "июня",
             "07": "июля",
             "08": "августа",
             "09": "сентября",
             "10": "октября",
             "11": "ноября",
             "12": "декабря"}


    date_num = {"01": "Первое", "02": "Второе", "03": "Третье", "04": "Четвертое", "05": "Пятое", "06": "Шестое"}

    date_input = input("Введи дату в формате дд.мм.гггг : ")

    tek_date = f"Дата: {date_num[date_input[:2]]} {month[date_input[3:5]]} {date_input[6:]} года"

    print(tek_date)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random


def zadanie3():

    my_list = list()
    n = input("Введи количество элементов : ")
    n = int(n)

    while n > 0:
        my_list.append(random.randrange(-100, 100))
        n = n -1

    for i in my_list:
        print(i)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
def zadanie4():

    my_list = [1, 2, 4, 5, 6, 2, 5, 2]
    final_list = list()

    print("неповторяющиеся элементы исходного списка:")
    print(set(my_list))

    test_list = set(my_list)
    n=0

    for item in test_list:
        for item2 in my_list:
            if item == item2:
                n=n+1

        if 0 < n < 2:
            final_list.append(item)
            n=0
            continue
        n=0

    print("Элементы, которые не имеют повторений: ")
    print(final_list)




select = input("Введи номер задачи 1-4 \n")

if select == "1":
    zadanie1()
elif select == "2":
    zadanie2()
elif select == "3":
    zadanie3()
elif select == "4":
    zadanie4()
else:
    print("Неправильный ввод")
