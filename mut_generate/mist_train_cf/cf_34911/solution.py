"""
QUESTION:
Create a function `determine_winner(user_choice, computer_choice)` that determines the winner of a game of rock-paper-scissors based on the user's choice and the computer's choice. The function should take two parameters: `user_choice` and `computer_choice`, both of which are strings representing the user's choice and the computer's choice, respectively. The function should return a string indicating the result of the game: "You win!", "You lose!", or "It's a draw!". The game rules are as follows: rock beats scissors, scissors beats paper, and paper beats rock.
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