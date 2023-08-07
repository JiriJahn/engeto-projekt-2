"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
import random

def welcome_message():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

def generate_secret_number():
    digits = list(range(1, 10))  # Číslice 1 až 9 (nezahajující 0)
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def validate_guess(guess):
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) < 4 or guess[0] == "0":
        return False
    return True

def evaluate_guess(secret_number, guess):
    bulls = sum(1 for i in range(4) if secret_number[i] == guess[i])
    cows = sum(1 for digit in secret_number if digit in guess) - bulls
    return bulls, cows

def main():
    welcome_message()
    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter a number: ")

        if not validate_guess(guess):
            print("Invalid input. Please enter a 4-digit number with unique non-zero digits.")
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            break

        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

if __name__ == "__main__":
    main()
