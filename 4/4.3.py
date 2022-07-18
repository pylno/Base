#ntrcn

player = {
    'name': input('Введите имя героя:'),
    'health': 100,
    'damage': 50
}

enemy = {
    'name': input('Введите имя злодея:'),
    'health': 100,
    'damage': 50
}

def attack(unit, target):
    target ['health'] -= unit ['damage']

attack(player, enemy)
print(enemy)
attack(enemy, player)
print(player)