from random import randint, choice
numbers = []
# Получаем случайный список из 15 чисел от 10 до 100
for i in range(15):
    numbers.append(randint(10, 100))
print(numbers)

numbers = []
# Делаем функцию по поиску случайных чисел
def rd_num(numbers):
    if numbers:
        return choice(numbers)

print(rd_num(numbers))