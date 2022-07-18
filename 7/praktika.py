#Тернарный оператор
# is_has_name = True
# name = 'Yulia' if is_has_name else 'Empty'
# print(name)

word = 'привет'
result = []

#Без тернарного оператора
# for i in range(len(word)):
#     if i%2 == 0:
#         letter = word[i].lower()
#     else:
#         letter = word[i].upper()
#     result.append(letter)
# result = ''.join(result)
# print(result)

#С тернарным оператором
# for i in range(len(word)):
#     letter = word[i]
#     letter = letter.lower() if i%2 == 0 else letter.upper()
#     result.append(letter)
# result = ''.join(result)
# print(result)

# Пример пароля
# password = input('Введите пароль: ')
#
# print('Вход разрешен' if password == 'secret' else 'Вход запрещен')

#Пример двойного пароля
# password = input('Введите пароль: ')
# new_password = input('Введите пароль: ')
#
# print('Вход разрешен' if new_password == password else 'Вход запрещен')