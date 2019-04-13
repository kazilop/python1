__author__ = 'Рыбка Артем Сергеевич'

import math
import random


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def zadanie1():
    def fibinacci(n,m):

        if n > 2:

            numb1 = 1
            numb2 = 1
            fib = list()
            i = 1

            while i <= m-2:
                summ = numb1 + numb2
                fib.append(summ)
                numb1 = numb2
                numb2 = summ
                i += 1
        else:
            return 1
        return fib[n-3:i]

    print(fibinacci(6, 15))



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def zadanie2():
    def sort_to_max(origin_list):
        for i in range(len(origin_list)):
            i_min = i
            for a in range(i+1, len(origin_list)):
                if origin_list[a] < origin_list[i_min]:
                    i_min = a
            buffer = origin_list[i_min]
            origin_list[i_min] = origin_list[i]
            origin_list[i] = buffer
        return origin_list

    result = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
    print("Начальный список : ")
    print([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
    print("Отсортированный список : ")
    print(result)


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def zadanie3():

    my_list = ['true', 'false', 'privet', 'true', 'fire']

    def my_filter(f, my_list):
        new_list = list()
        for item in my_list:
            new_list.append(f(item))
        return new_list

    print(my_filter(len, my_list))




# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def zadanie4():
    p1 = (10, 15)
    p2 = (18, 15)
    p3 = (21, 6)
    p4 = (13, 6)

    def dlinna(point1, point2):
        """ расстрояние между точками """
        d = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
        return d

    def is_parell(t1, t2, t3, t4):
        if t2[0] - t1[0] == t3[0] - t4[0]:   # равна ли длина гориз. сторон
            if t1[1] - t4[1] == t2[1] - t3[1]: # равна ли длина вертикальных сторон
                    # Сумма квадратов диагоналей параллелограмма равна сумме квадратов его сторон
                if (dlinna(t4,t2)**2 + dlinna(t1,t3)**2) == (2* dlinna(t4,t1)**2 + 2*dlinna(t1,t2)**2):
                    return "Параллелограмм"
                else:
                    return "Условия не выполняются"
            else:
                return "Условия не выполняются"
        else:
            return "Условия не выполняются"

    print(is_parell(p1,p2,p3,p4))


    return 0




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
