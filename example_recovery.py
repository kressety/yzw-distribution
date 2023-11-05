from os import remove
from os.path import exists
from shutil import copy2


def example_recover():
    if exists('example.xlsx'):
        remove('example.xlsx')
    copy2('src/example.xlsx', 'example.xlsx')
