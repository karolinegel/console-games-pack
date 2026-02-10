print("Guess the Number Game")
import random

def generate_number():
    return random.randint(1, 10)

print("Guess the Number Game")
def check_guess(secret, guess):
    return secret == guess
