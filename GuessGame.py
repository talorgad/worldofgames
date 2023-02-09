import random

def generate_number():
    global diff_num, secret_number
    while True:
        try:
            diff_num = int(input("please enter the difficulty level number: "))
            secret_number = int(random.uniform(1, diff_num))
        except ValueError:
            print("You must select a number, please try again ")
            continue
        if diff_num < 1:
            print("please select a number greater than 1 ")
            continue
        break
    return diff_num, secret_number

difficulty = generate_number()

def get_guss_from_user():
    while True:
        user_guss = int(input(f"please make a guess between 1 to {difficulty[0]}: "))
        if not 1 <= user_guss <= difficulty[0]:
            print(f"number is not in the range, please select a number between 1 - {difficulty[0]} ")
        else:
            return user_guss

guss_num = get_guss_from_user()

def compare_results():
    if difficulty[1] == guss_num:
        return "TRUE"
    else:
        return "FALSE"

result = compare_results()
print(result)


def play():
    generate_number()
    get_guss_from_user()
    compare_results()
