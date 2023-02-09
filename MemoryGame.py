import time
import os
from os import system, name
from Utils import clear_console




def generate_sequence():
    import random
    global difficulty, random_list
    while True:
        try:
            difficulty = int(input("please enter the difficulty level number: "))
            random_list = []
            for i in range(0, difficulty):
                n = random.randint(1, 101)
                random_list.append(n)
            print(random_list)
            time.sleep(difficulty)
            clear_console()
            break
        except ValueError:
            print("You must select a number, please try again ")
        break
    return difficulty


def get_list_from_user():
    global guss_list
    input_list = input(f"please guss {difficulty} numbers separated by space \n")
    guss_list = input_list.split()
    for i in range(len(guss_list)):
        guss_list[i] = int(guss_list[i])
    # print(guss_list)


def is_list_equal():
    global is_win
    if random_list == guss_list:
        print("correct!! you are the winner!!!!")
        is_win = True
    else:
        print("wrong answer... you lost")
        is_win = False
        return is_win


def save_score():
    if is_win == True:
        score = (diffculty*3)+5
        print(f"your score is: {score}")
        return score


def play():
    generate_sequence()
    get_list_from_user()
    is_list_equal()


play()