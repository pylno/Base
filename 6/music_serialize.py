# Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
import pickle
import json

my_favourite_group = {
'name': 'Vitamin String Quartet',
'tracks': ['Home', 'Плохой парень'],
'Albums': [{'name': 'Performs Muse', 'year': 2010},
{'name': "Radiohead's 'In Rainbows''", 'year': 2009}]
}

#Pickle
with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
print('Объект pickle записан')

with open('group.pickle', 'rb') as f:
    result = pickle.load(f)
print(result)
print('Смотрим, как оно')
print(pickle.dumps(my_favourite_group))

#Json
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)
print('Объект json записан')

with open('group.json', 'r') as f:
    result = json.load(f)
print(result)
print('Смотрим, как оно')
print(json.dumps(my_favourite_group))
