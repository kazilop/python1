
__author__ = 'Рыбка Артем Сергеевич'

import math
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def zadanie1():

    def my_round(number, ndigits):
        number = number * (10 ** ndigits)

        number = number // 1
        return number / (10 ** ndigits)

    print(my_round(5435225.44444, 2))






# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def zadanie2():

    def lucky(numb):
        first_dig = int(numb[0]) + int(numb[1]) + int(numb[2])
        second_dig = int(numb[3]) + int(numb[4]) + int(numb[5])

        if first_dig == second_dig:
            return "Lucky"
        else:
            return "Not lucky :("

    my_input = input("Введи 6-значное число: \n")
    print(lucky(my_input))

# ##########################################################


select = input("Введи номер задачи (1-2) \n")

if select == "1":
    zadanie1()
elif select == "2":
    zadanie2()

else:
    print("Неправильный ввод")
