"""
QUESTION:
Write a function `check_game_status` that takes two lists of cards and two prestige values as input and returns a string indicating the game status. The function should check if either player has no more cards or if their prestige is zero or negative. If the game has ended, the function should return a string indicating the winner or if there is a tie.
"""

def check_game_status(player1_cards, player2_cards, player1_prestige, player2_prestige):
    if not player1_cards or not player2_cards or player1_prestige <= 0 or player2_prestige <= 0:
        if player1_prestige > player2_prestige:
            return "Player 1 wins!"
        elif player2_prestige > player1_prestige:
            return "Player 2 wins!"
        else:
            return "It's a tie!"