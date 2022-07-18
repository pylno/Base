#машина угадывает число
import random
min_number = 1
max_number = 100
result = None

while result != '=':
    machine_number = random.randint(min_number, max_number)
    print(machine_number)
    result = input('меньше больше =')

    if result == 'больше':
        min_number = machine_number + 1
        pass
    else:
        max_number = machine_number - 1
print("Победа")



