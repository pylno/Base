#Написать функцию, которая принимает на вход число от 1 до 100.
# Если число равно 13, функция поднимает исключительную ситуации ValueError
# иначе возвращает введенное число, возведенное в квадрат.
#Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат,
# который вернула функция. Обработать возможность возникновения исключительной ситуации,
# которая поднимается внутри функции.
import random

#numb = random.randint(1, 100)
# numb = 10
#
# def my_func(numb):
#     try:
#         if numb != 13:
#             result = numb ** 2
#             print(result)
#     except:
#         numb == 13
#         print('ValueError')
#
# my_func(numb)


def my_func(numb):
    if numb != 13:
        result = numb ** 2
        print(result)
    if numb == 13:
        raise ValueError('Несчастливое число')


my_numb = int(input('Введите число: '))

try:
    my_func(my_numb)
except ValueError:
    print('Не надо 13')

# Его решение
def unlucky_number(number):
    if number == 13:
        raise ValueError('Несчастливое число')
    else:
        return number ** 2

number = int(input('Введите число: '))
try:
    result = unlucky_number(number)
except ValueError:
    print('No 13')
else:
    print(result)

