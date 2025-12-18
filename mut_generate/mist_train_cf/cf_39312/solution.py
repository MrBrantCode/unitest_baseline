"""
QUESTION:
Create a function `determine_winner` that determines the winner of a game of rock-paper-scissors based on the user's choice and the computer's choice. The function should take two parameters, `user_choice` and `computer_choice`, both of which are strings representing the choices. The function should return a string indicating the result of the game. The rules of the game are as follows: rock beats scissors, scissors beats paper, and paper beats rock. If the user and the computer make the same choice, the result is a tie.
"""

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"