import random
favorite_fruits = ['apple', 'banana', 'orange', 'melon', 'sandia']
word_list = favorite_fruits
word = random.choice(word_list)

# Hangman Project: Milestone 3 - Task 1

while True:
    guess = input("Guess a letter: ")

    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# Hangman Project: Milestone 3 - Task 2

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")


# Hangman Project: Milestone 3 - Task 3

def check_guess(guess):
    guess = guess.lower()
    
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        check_guess(guess)
        break

ask_for_input()

# Hangman Project: Milestone 2 - Task 4 - ReadMe file

# Hangman Project: Milestone 2 - Task 5 - Update code to GitHub

# Hangman Project: Milestone 2 - Task 6 - Optimise current code 