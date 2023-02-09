def welcome(name):
    # name = input(print("please enter your name: "))
    print(f"Hello {name} and welcome to the World of Games (WoG)" + "\n" + "here you can find many cool games to play." + "\n")

# welcome()


def load_game():

    # game_map = {
    #     1: play_mg,
    #     2: play_gg,
    #     3: play_cr
    # }
    while True:
        try:
            chosen_game = int(input("""Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS
                """))
        except ValueError:
            print("You must select the game number, please try again ")
            continue
        if not 1 <= chosen_game <= 3:
            print("please select between 1 to 3 ")
            continue
        break

    game_map[chosen_game]()


load_game()