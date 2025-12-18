"""
QUESTION:
Implement a function `is_game_over` that takes four arguments: `player_one_cards`, `player_one_prestige`, `player_two_cards`, and `player_two_prestige`. The function should return `True` if the game is over (i.e., one player has no cards or zero/negative prestige) and `False` otherwise. Additionally, it should print a message indicating the winner when the game is over.
"""

def is_game_over(player_one_cards, player_one_prestige, player_two_cards, player_two_prestige):
    if not player_one_cards or player_one_prestige <= 0:
        print("Player 2 wins! Game over.")
        return True
    elif not player_two_cards or player_two_prestige <= 0:
        print("Player 1 wins! Game over.")
        return True
    else:
        return False