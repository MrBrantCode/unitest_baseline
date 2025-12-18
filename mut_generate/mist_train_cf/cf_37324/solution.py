"""
QUESTION:
Implement a function `calculate_exp_required(level)` that calculates the experience points required for a Pokémon to reach a certain level. The function takes an integer level greater than 0 as input and returns the experience points required, rounded down to the nearest integer, using the formula EXP = floor(4 * level^3 / 5).
"""

def calculate_exp_required(level):
    exp_required = int(4 * (level ** 3) / 5)
    return exp_required