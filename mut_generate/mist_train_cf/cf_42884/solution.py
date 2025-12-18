"""
QUESTION:
Create a `BettingGame` class with a `validate_bet` method that checks if a player's bet is valid. The method should take `player_bet` as a parameter and return `False` if the player wants to exit the game (using a case-insensitive match with valid exit commands provided during class initialization) or if the bet is not a positive integer. Otherwise, it should return `True`.
"""

import re

def validate_bet(player_bet, valid_exit_commands):
    if player_bet.lower() in valid_exit_commands:
        return False
    if re.match(r'^\s*[0-9]+\s*$', player_bet):
        return True
    else:
        return False