# CodeAlpha Task 1: Hangman Game
# Simple text-based Hangman game using Python

import random

# Predefined list of words
words = ["python", "computer", "program", "developer", "coding"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
max_attempts = 6
wrong_guesses = 0

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses allowed.")

# Create hidden word display
display = ["_"] * len(word)

# Game loop
while wrong_guesses < max_attempts and "_" in display:

    print("\nWord:", " ".join(display))
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check letter in word
    if guess in word:
        print("Correct guess!")

        for index in range(len(word)):
            if word[index] == guess:
                display[index] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)

else:
    print("\nGame Over!")
    print("The correct word was:", word)
