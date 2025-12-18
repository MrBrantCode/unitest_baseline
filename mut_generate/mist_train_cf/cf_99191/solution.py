"""
QUESTION:
Create a function `game_ended` that checks if a card game between two players has ended. The function takes four parameters: the remaining cards of player 1 (`player1_cards`), the remaining prestige of player 1 (`player1_prestige`), the remaining cards of player 2 (`player2_cards`), and the remaining prestige of player 2 (`player2_prestige`). The function should return `True` and print a message indicating the winner if the game has ended, and `False` otherwise. The game ends when one of the players has no cards left or their prestige is less than or equal to 0.
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