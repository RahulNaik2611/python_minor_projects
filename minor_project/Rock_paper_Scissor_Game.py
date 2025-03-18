import random

# Get user input
user_Input = input("Enter your choice (Rock, Paper, Scissors): ").lower()

# Computer's random choice
computer_choices = ['rock', 'paper', 'scissors']
Game = random.choice(computer_choices)

# Display choices
print(f"Computer chose: {Game.capitalize()}")

# Game logic
if user_Input == Game:
    print("It's a draw!")
elif (user_Input == "rock" and Game == "paper") or \
     (user_Input == "paper" and Game == "scissors") or \
     (user_Input == "scissors" and Game == "rock"):
    print("Computer wins!")
elif (user_Input == "rock" and Game == "scissors") or \
     (user_Input == "paper" and Game == "rock") or \
     (user_Input == "scissors" and Game == "paper"):
    print("You win!")
else:
    print("Invalid input. Please choose Rock, Paper, or Scissors.")
