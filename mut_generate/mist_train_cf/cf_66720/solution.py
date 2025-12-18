"""
QUESTION:
Write a function 'play_game' that takes two parameters, player1 and player2, representing the choices of the two players in a game of rock paper scissors lizard Spock. The function should return the outcome of the game based on the following rules:

- Scissors cuts Paper.
- Paper covers Rock.
- Rock crushes Lizard.
- Lizard poisons Spock.
- Spock smashes Scissors.
- Scissors decapitates Lizard.
- Lizard eats Paper.
- Paper disproves Spock.
- Spock vaporizes Rock.
- Rock crushes Scissors.

If both players make the same choice, the function should return "Draw". Otherwise, it should return "Player 1 wins" if player1's choice beats player2's choice, and "Player 2 wins" otherwise.
"""

def entance(player1, player2):
    if player1 == player2:
        return "Draw"
    if (player1 == 'Rock' and player2 in ['Scissors', 'Lizard']) or \
       (player1 == 'Paper' and player2 in ['Rock', 'Spock']) or \
       (player1 == 'Scissors' and player2 in ['Paper', 'Lizard']) or \
       (player1 == 'Lizard' and player2 in ['Spock', 'Paper']) or \
       (player1 == 'Spock' and player2 in ['Scissors', 'Rock']):
        return "Player 1 wins"
    return "Player 2 wins"