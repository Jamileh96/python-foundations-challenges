# --- TROUBLESHOOTING NOTES ---
# 1. THE "MEMORY" FIX:
# Replace: print(input("Guess again."))
# With: guess = int(input("Guess again: "))
# Why? You must save the new input into the 'guess' variable
# so the 'while' loop has a new number to check.
import random
def game(lives, random_number):
    guess = int(input("Guess the number: "))
    game_start = True
    while game_start:
        if guess > random_number:
            game_start = True
            print("Too high!")
            lives = lives - 1

            if lives == 0 and guess != random_number:
                print("You ran out of lives!GAME OVER")
                return

            print(f"you have {lives} attempts to guess the number.")
            guess = int(input("Guess again."))

        elif guess < random_number:
            game_start = True
            print("Too low!")
            lives = lives - 1

            if lives == 0 and guess != random_number:
                print("You ran out of lives!GAME OVER")
                return

            print(f"you have {lives} attempts to guess the number.")
            guess = int(input("Guess again."))



print("Welcome to the Number Guessing Project")
print("I am thinking of a number between 1 and 100")

game_level = str(input("Chose a difficulty. Type 'easy' or 'hard'")).lower()
EASY_LEVEL = 10
HARD_LEVEL = 5
number =random.randint(1, 100)
if game_level == "easy":
    print("You have 10 attempts to guess the number.")
    game(lives=EASY_LEVEL, random_number=number)

if game_level == "hard":
    print("You have 5 attempts to guess the number.")
    game(lives=HARD_LEVEL, random_number=number)


