"""
QUESTION:
Create a function `determine_winner(user_choice, computer_choice)` that takes two parameters, the user's choice and the computer's choice, where the choice can be either "rock", "paper", or "scissors". The function should return the result of the game based on the following rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock
The function should return one of three possible outcomes: "You win!", "You lose!", or "It's a draw!".
"""

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"