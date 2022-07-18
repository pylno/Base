#Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
my_list_1 = [2, 5, 8, 5, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
# my_list_1 = set(my_list_1)
# my_list_2 = set(my_list_2)

for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)



# result = my_list_1 - simular
# simular = (my_list_1 & my_list_2)
# print(my_list_1 - simular)


# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
#
# if x in simular and my_list_1:
#     my_list_1.pop(sim)
# print(my_list_1)

# my_list_1.pop(i) for i in simular:
#     print(my_list_1)

#[li.append(i) for i in my_list if i not in li]

#removed = my_list_1.pop(i)

# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# for i in my_list_1:
#     if i in simular:
#         del my_list_1 [i]
# print(my_list_1)



