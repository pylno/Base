import sys
import random
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir

from game import game_comp

save_info('start')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. Например, help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print("Отсутствует название файла")
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print("Отсутствует название файла")
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print("Отсутствует название файла")
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print("Отсутствует название обоих файлов")
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file пробел название файла и расширение - создание файла')
        print('create_folder пробел название файла и расширение - создание папки')
        print('delete пробел название файла и расширение - удаление файла или папки')
        print('copy пробел название файла и расширение пробел название нового файла и расш. - копирование файла или папки')
        print('game - игра')
        print('ch - смена директории')

    elif command == 'ch':
        try:
            name = sys.argv[2]
        except NameError:
            print("Отсутствует название директории")
        else:
            change_dir(name)
    elif command == 'game':
        game_comp()

save_info('end')
