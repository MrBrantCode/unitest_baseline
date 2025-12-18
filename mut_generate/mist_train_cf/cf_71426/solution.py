"""
QUESTION:
Write a function `determine_winner(player_move, computer_move)` that determines the winner of a game of rock paper scissors given the player's move and the computer's move. The function should return a string stating the result of the game, such as "It's a tie!", "Player wins!", or "Computer wins!". The function should assume that the input moves are either 'rock', 'paper', or 'scissors'.
"""

def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == 'rock' and computer_move == 'scissors') or \
        (player_move == 'scissors' and computer_move == 'paper') or \
        (player_move == 'paper' and computer_move == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"