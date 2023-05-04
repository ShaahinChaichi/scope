import random


def play(level):
    random_number = random.randrange(1, 100)
    print(random_number)
    is_game_over = False
    if level == "easy":
        while not is_game_over:
            for play_number in range(9):
                guess_number = int(input("Please guess a number: "))
                if guess_number > random_number:
                    print("Too high, guess again")
                    print(f"Number of guess {9 - play_number}")
                    play_number += 1
                elif guess_number < random_number:
                    print("Too low, guess again")
                    print(f"Number of guess {9 - play_number}")
                    play_number += 1
                else:
                    print("Success")
                    start_of_project()

    while not is_game_over:
        if level == "hard":
            for play_number in range(5):
                guess_number = int(input("Please guess a number: "))
                if guess_number > random_number:
                    print("Too high, guess again")
                    print(f"Number of guess {5 - play_number}")
                    play_number += 1
                elif guess_number < random_number:
                    print("Too low, guess again")
                    print(f"Number of guess {5 - play_number}")
                    play_number += 1
                else:
                    print("Success")
                    is_game_over = True
                    start_of_project()


def start_of_project():
    continue_game = input("Do you want to continue? ('y' or 'n') ")
    if continue_game == 'y':
        easy_or_hard = input("'easy' or 'hard' ?")
        play(easy_or_hard)
    else:
        print("Thanks for playing !!!!")
        return


start_of_project()
