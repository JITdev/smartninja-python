import random
import json

end = 5
secret = random.randint(1, end)
guess = 0
tries = 5
num = {}

for x in range(tries):
    print(f'Az {x+1}. probalkozas')
    guess = int(input(f"Guess the secret number (between 1 and {end}): "))
    num[str(x)] = guess

    if guess == secret:
        print("You've guessed it - congratulations! It's number .")
        with open("score.txt", "r+") as score_file:
            score = score_file.read()
            if not score or (score and int(score)<int(guess)):
                score_file.seek(0)
                score_file.write(str(guess))
        break
    elif x == tries-1:
        print(f"You lost, the secret number is: {secret}")
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

with open("score.txt", "r") as score_file:
    best_score = score_file.read()
    print("Top score: " + best_score)

with open("score_list.txt", "w") as score_file:
    score_file.write(json.dumps(num))
