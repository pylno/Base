from random import randint, choice

def get_random(input_list):
    if input_list:
        result = (choice(input_list))
        return result
print(get_random([1, 2, 3, 4]))
print(get_random([]))