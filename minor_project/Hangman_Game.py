import random

# ASCII art for hangman stages (progressively worse)
hangman_stages = [
    """
     ------
     |    |
     |
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---
    """
]

words_list = ['rahul', 'teju', "balu", "python", "hangman", "programming"]
secret_word = random.choice(words_list).lower()
print("Hint: The word has", len(secret_word), "letters")

# Initialize variables
display = ["_"] * len(secret_word)
correct_letters = []
incorrect_guesses = 0
max_attempts = len(hangman_stages) - 1  # Matches number of stages
game_over = False

print(" ".join(display))  # Show initial blank spaces

while not game_over:
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    if guess in correct_letters:
        print("You already guessed that letter!")
        continue

    # Check if guess is in the word
    if guess in secret_word:
        # Update display with correctly guessed letters
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display[i] = guess
        correct_letters.append(guess)
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Incorrect!")
        print(hangman_stages[incorrect_guesses])  # Show hangman progress
        print(f"You have {max_attempts - incorrect_guesses} attempts left.")

    # Show current progress
    print("\nCurrent word:", " ".join(display))

    # Check win/lose conditions
    if "_" not in display:
        game_over = True
        print("\nCongratulations! You won!")
    elif incorrect_guesses >= max_attempts:
        game_over = True
        print(hangman_stages[-1])  # Show full hangman
        print(f"\nGame over! The word was: {secret_word}")