import random

random_number = random.randrange(1, 100)


def play(level):
    print(random_number)
    if level == "easy":
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


easy_or_hard = input("'easy' or 'hard' ?")

play(easy_or_hard)
