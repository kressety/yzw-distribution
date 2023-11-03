from os import remove
from os.path import exists
from os import system


def example_recover():
    if exists('example.xlsx'):
        remove('example.xlsx')
    system('wget https://src.mealuet.com/example.xlsx')
