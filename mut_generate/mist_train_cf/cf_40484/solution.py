"""
QUESTION:
Create a function `rock_paper_scissors` that takes two arguments: `player_choice` and `computer_choice`. The function should determine the winner based on the standard rules of rock-paper-scissors (rock beats scissors, scissors beats paper, paper beats rock) and return the result. The function should return 'It's a tie!' if the choices are the same, 'Player wins!' if the player wins, and 'Computer wins!' otherwise.
"""

def rock_paper_scissors(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'Player wins!'
    else:
        return 'Computer wins!'