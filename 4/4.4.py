
player = {
    'name': input('Введите имя героя:'),
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy = {
    'name': input('Введите имя злодея:'),
    'health': 50,
    'damage': 30,
    'armor': 1
}

def attack(unit, target):
    target ['health'] -= (unit ['damage'] / target ['armor'])

attack(player, enemy)
print(enemy)
attack(enemy, player)
print(player)