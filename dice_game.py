import random

def roll_dice():
    return random.randint(1, 6)

print("Dice rolled:", roll_dice())

def play_dice():
    result = roll_dice()
    print(f"You rolled {result}")

if __name__ == "__main__":
    play_dice()
