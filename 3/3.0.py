# я угадываю число машины
number = random.randint(1, 100)

while True:
    guess = int(input('Введите число:'))
    if guess == number:
        print('Вы угадали')
        break
    elif guess > number:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')