import os
from os import system, name

SCORES_FILE_NAME = "C:\\Users\ortal\PycharmProjects\WorldOfGames\Scores.txt"
BAD_RETURN_CODE = "3333"


def clear_console():
    if name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')