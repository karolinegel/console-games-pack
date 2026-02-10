print("Guess the Number Game")
import random

def generate_number():
    return random.randint(1, 10)

print("Guess the Number Game")
def check_guess(secret, guess):
    return secret == guess
secret = generate_number()
guess = int(input("Enter number 1-10: "))

if check_guess(secret, guess):
    print("You win")
else:
    print("You lose")
def play_guess_game():
    secret = generate_number()
    guess = int(input("Enter number 1-10: "))
    print("Win" if check_guess(secret, guess) else "Lose")

if __name__ == "__main__":
    play_guess_game()
 
