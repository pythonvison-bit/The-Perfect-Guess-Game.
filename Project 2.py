# The Perfect Guess Game

import random

print("The Perfect Guess Game")

r = random.randint(1, 100)

a = -1

guesses = 0

while a != r:
    a = int(input("Enter your guess: "))
    guesses += 1

    if a < r:
        print("Too low! Try again.")
    elif a > r:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {r} in {guesses} attempts.")


