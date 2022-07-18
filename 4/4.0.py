#Запросить три числа, найти макс, мин и их сумму
list_1 = []

# number_1 = int(input('Введите первое число: '))
# list_1.append(number_1)
# number_2 = int(input('Введите второе число: '))
# list_1.append(number_2)
# number_3 = int(input('Введите третье число: '))
# list_1.append(number_3)
for i in range (3):
    number = int(input('Введите число: '))
    list_1.append(number)



print(f'Самое большое число: {max(list_1)}')
print(f'Самое маленькое число: {min(list_1)}')
print(f'Cумма чисел: {sum(list_1)}')