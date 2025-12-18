"""
QUESTION:
Write a function named `determine_winner` that takes two parameters, `user_choice` and `computer_choice`, both of which can be 'rock', 'paper', or 'scissors'. The function should compare the two choices and return the outcome of the game. The game's rules are: rock beats scissors, scissors beats paper, and paper beats rock. If both choices are the same, the function should return "It's a draw!". If the user wins, the function should return "You win!". If the computer wins, the function should return "You lose!".
"""

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"