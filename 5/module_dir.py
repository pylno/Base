import os


def get_dirs():
    for i in range(1, 10):
        name = f'dir_{str(i)}'
        print(name)
        os.mkdir(name)


get_dirs()