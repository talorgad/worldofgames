from MemoryGame import save_score

score = save_score()

def add_score():
    file = open("Scores.txt", "w")
    file.write(f"your score is: {score}")
    file.close()
    file = open("Scores.txt", "r")
    content = file.read()
    print(content)
    file.close()


add_score()

# import os
#     file_path = os.path.join(r"C:\Users\ortal\PycharmProjects\WorldOfGames", "Scores.txt")
# with open(file_path, 'w') as f:
#     f.write('Create a new text file!!!!')
#
# print(SCORES_FILE_NAME)
# # BAD_RETURN_CODE - A number representing a bad return code for a function.
# def save_score(score, filename="Scores.txt"):
#     with open(filename, "a") as f:
#         f.write(f"{score}\n")
# def play_gg():
#     generate_number()
#     guss_num = get_guss_from_user()
#     check = compare_results()
#     score = 0
#     if check == "TRUE":
#         score = 1
#     with open("Scores.txt", "a") as file:
#         file.write(str(score) + "\n")
#     with open("Scores.txt", "r") as file:
#         scores = file.readlines()
#     total_score = sum([int(score.strip()) for score in scores])
#     return total_score
#
#
# def screen_cleaner():
#     os.system("""python C:\\Users\\ortal\\PycharmProjects\\WorldOfGames\\ToSend\\level_3\\clear.py""")
#
#
# screen_cleaner()
