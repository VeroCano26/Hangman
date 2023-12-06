# Hangman Project: Milestone 2 - Task 1
favorite_fruits = ['apple', 'banana', 'orange', 'melon', 'sandia']
word_list = favorite_fruits
print(word_list)

# Hangman Project: Milestone 2 - Task 2
import random
favorite_fruits = ['apple', 'banana', 'orange', 'melon', 'sandia']
word_list = favorite_fruits
word = random.choice(word_list)

# Hangman Project: Milestone 2 - Task 3
print(word)
guess = input("Enter a single letter: ")
print("User entered:", guess)

# Hangman Project: Milestone 2 - Task 4
if len(guess) == 1 and guess.isalpha():
   print("Good guess!")
else:
   print("Oops! That is not a valid input.")
