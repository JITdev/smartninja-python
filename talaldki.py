import random
import json

def play_game(tries = 5, end = 5):
    """ A jatek elinditasa

    :param tries: probalkozasok szama
    :param end: veletlen szam tartomany
    :return:
    """
    guess = 0
    secret = random.randint(1, end)
    score_list = []

    for x in range(tries):
        print(f'Az {x + 1}. probalkozas')
        guess = int(input(f"Guess the secret number (between 1 and {end}): "))
        score_list.append(guess)

        if guess == secret:
            print("You've guessed it - congratulations! It's number .")
            set_top_scores(x)
            break
        elif x == tries - 1:
            print(f"You lost, the secret number is: {secret}")
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

    set_score_list(score_list)


def set_score_list(score_list: list) -> None:
    with open("score_list.txt", "w") as score_file:
        score_file.write(json.dumps(score_list))

def set_top_scores(score: int):
    """ Az utolso 3 legjobb eredmeny

    Meg kell nyitni a fajlt, json.loads()
    score_list valtozoba tegyuk be > adjuk hozza a score valtozot
    rendezzuk a listat: sort()
     .write(json.dumps(score_list[:3]))
    """
    pass

def get_score_list():
    return

def get_top_scores():
    raise NotImplementedError


with open("score.txt", "r") as score_file:
    best_score = score_file.read()
    print("Top score: " + best_score)
