#Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
#После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
#Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
num = int(input("Напишите число:"))

while num > 10 or num < 0:
    print('Введите другое число от 0 до 10')
    num = int(input("Напишите число:"))
print(num ** 2)

# Как было в разборе
# while True:
#     num = int(input("Напишите число:"))
#     if num >= 10 or num <= 0:
#         print(num ** 2)
#         break
#     else:
#         print('Введите другое число от 0 до 10')