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
    guess_list = []

    for x in range(tries):
        print(f'Az {x + 1}. probalkozas')
        guess = int(input(f"Guess the secret number (between 1 and {end}): "))
        guess_list.append(guess)

        if guess == secret:
            print(f"You've guessed it - congratulations! It's number {secret}.")
            set_top_scores(x+1)
            break
        elif x == tries - 1:
            print(f"You lost, the secret number is: {secret}")
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

    set_guess_list(guess_list)


def set_guess_list(score_list: list) -> None:
    with open("score_list.txt", "w") as score_file:
        score_file.write(json.dumps(score_list))

def set_top_scores(score: int):
    """ Az utolso 3 legjobb eredmeny """
    with open("score.txt", "r+") as score_file:
        score_list = json.loads(score_file.read())
        score_list.append(score)
        score_list.sort()
        score_json = json.dumps(score_list[:3])
        score_file.seek(0)
        score_file.write(score_json)

def get_guess_list():
    with open("score_list.txt", "r") as score_file:
        guesses = score_file.read()
        print("Top score: " + guesses)

def get_top_scores():
    with open("score.txt", "r") as score_file:
        best_scores = score_file.read()
        print("Top score: " + best_scores)

play_game()