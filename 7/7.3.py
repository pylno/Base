# Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат
# (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
import math

# input_list = list(map(int, input('Введите значения списка через пробел ').split(' ')))
#
#
# def my_func(input_list):
#     result = [number**0.5 for number in input_list]
#     print(result)
#
# my_func(input_list)


# Интересная проверка на инт
# lst = [25, 36, 49, - 10]
# def new_sqrt(input_list):
#     result = [number**0.5 for number in input_list if float.is_integer(number**0.5)]
#     print(result)
#
# new_sqrt(lst)


lst = [25, -5, 36, 49, - 10]

def new_sqrt(input_list):
    result = [number**0.5 if number > 0 else number for number in input_list]
    return result


result = new_sqrt(lst)
print(result)
print(lst)
