import random
import json

class Game():
    def __init__(self, tries=5, end=5):
        self.tries = tries
        self.end = end
        self.guess = 0
        self.secret = random.randint(1, end)
        self.guess_list = []
        self.score = None
        self.score_list = None

    def play_game(self):
        """ A jatek elinditasa

        :param tries: probalkozasok szama
        :param end: veletlen szam tartomany
        :return:
        """

        for x in range(self.tries):
            print(f'Az {x + 1}. probalkozas')
            self.guess = int(input(f"Guess the secret number (between 1 and {end}): "))
            self.guess_list.append(self.guess)

            if self.guess == self.secret:
                print(f"You've guessed it - congratulations! It's number {self.secret}.")
                self.set_top_scores()
                break
            elif x == self.tries - 1:
                print(f"You lost, the secret number is: {secret}")
            elif self.guess > self.secret:
                print("Your guess is not correct... try something smaller")
            elif self.guess < self.secret:
                print("Your guess is not correct... try something bigger")

        self.set_guess_list()


    def set_guess_list(self):
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(self.score_list))

    def set_top_scores(self):
        """ Az utolso 3 legjobb eredmeny """
        with open("score.txt", "r+") as score_file:
            score_list = json.loads(score_file.read())
            score_list.append(self.score)
            score_list.sort()
            score_json = json.dumps(score_list[:3])
            score_file.seek(0)
            score_file.write(score_json)

    def get_guess_list(self):
        with open("score_list.txt", "r") as score_file:
            guesses = score_file.read()
            print("Top score: " + guesses)

    def get_top_scores(self):
        with open("score.txt", "r") as score_file:
            best_scores = score_file.read()
            print("Top score: " + best_scores)


game = Game()

game.play_game()