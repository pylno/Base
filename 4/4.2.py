#Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

list_1 = []

def my_func():
    for i in range (3):
        number = int(input('Введите число: '))
        list_1.append(number)
    result = print(f'Самое большое число: {max(list_1)}')
    return result

my_func()
