"""
QUESTION:
Create a function `determine_winner` that takes two parameters, `user_choice` and `computer_choice`, which can be 'rock', 'paper', or 'scissors'. The function should return 'You win!' if the user beats the computer, 'You lose!' if the computer beats the user, and 'Draw' if the choices are the same. The rules are: rock beats scissors, scissors beats paper, and paper beats rock.
"""

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"