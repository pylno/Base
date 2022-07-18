
def game_comp():
    import random
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

game_comp()

if __name__ = '__main__':
    game_comp()