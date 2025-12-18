"""
QUESTION:
Create a function `rock_paper_scissors(player1, player2)` that takes two string arguments representing the choices of two players in a game of rock-paper-scissors. The function should be case-insensitive and return the result of the game based on the standard rules. If the inputs are invalid, the function should return an error message. The possible return values are "Player 1 wins!", "Player 2 wins!", "It's a tie!", and "Invalid input, please enter 'rock', 'paper', or 'scissors'."
"""

def entrance(player1, player2):
    valid_inputs = {'rock', 'paper', 'scissors'}
    player1 = player1.lower()
    player2 = player2.lower()

    if player1 not in valid_inputs or player2 not in valid_inputs:
        return "Invalid input, please enter 'rock', 'paper', or 'scissors'."

    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"