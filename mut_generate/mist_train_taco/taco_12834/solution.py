"""
QUESTION:
# Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return `Draw!`.

Examples:

![rockpaperscissors](http://i.imgur.com/aimOQVX.png)
"""

def determine_winner(player1_choice, player2_choice):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    
    if beats[player1_choice] == player2_choice:
        return 'Player 1 won!'
    if beats[player2_choice] == player1_choice:
        return 'Player 2 won!'
    return 'Draw!'