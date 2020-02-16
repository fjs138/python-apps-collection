__author__ = 'frank'
from random import randint
secret = randint(1,10)
guess = 0
while guess != secret:
    guess = input("Guess the number I'm thinking of: ")
    guess = int(guess)
    if guess == secret:
        print("Corect!")
    else:
        print("Nope...")
        if guess>secret:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
print("Game Over")