import random

rrr = 'sztring'
# rrr.u
end = 10
secret = random.randint(1, end)
guess = 0
tries = 5

for x in range(tries):
    print(f'Az {x+1}. probalkozas')
    guess = int(input(f"Guess the secret number (between 1 and {end}): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number .")
        break
    elif x == tries-1:
        print(f"You lost, the secret number is: {secret}")
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")


# while guess != secret:
#     guess = int(input("Guess the secret number (between 1 and 10): "))
#     if guess == secret:
#         print("You've guessed it - congratulations! It's number " + str(secret))
#     else:
#         print(f'Sorry, your guess is not correct... The secret number is not {guess}')
