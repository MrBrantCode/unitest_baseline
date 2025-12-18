"""
QUESTION:
Create a function `game_ended` that takes four parameters: `player1_cards`, `player1_prestige`, `player2_cards`, and `player2_prestige`, all of which are required. The function should return `True` if the game has ended and `False` otherwise. The game is considered ended if either player has run out of cards or has a prestige of zero or less. If the game has ended, the function should print a message indicating which player has won.
"""

def game_ended(player1_cards, player1_prestige, player2_cards, player2_prestige):
    if player1_cards == [] or player1_prestige <= 0:
        print("Player 2 wins!")
        return True
    elif player2_cards == [] or player2_prestige <= 0:
        print("Player 1 wins!")
        return True
    else:
        return False