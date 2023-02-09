import random
import requests


def get_money_interval():
    global interval, amt
    endpoint = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(endpoint)
    data = response.json()
    rate = data["rates"]["ILS"]
    difficulty = int(input("please enter the difficulty level number: "))
    amt = int(random.uniform(1, 100))
    total_amt = rate * amt
    min_range = int(total_amt - difficulty)
    max_range = int(total_amt + difficulty)
    interval = [*range(min_range, max_range)]
    print(interval)
    return interval, amt


def get_guess_from_user():
    user_guess = float(input(f"please try to guess, how much ILS are {amt} USD? "))
    if user_guess in interval:
        print("correct")
    else:
        print("wrong")


def play_cr():
    get_money_interval()
    get_guess_from_user()


play_cr()
