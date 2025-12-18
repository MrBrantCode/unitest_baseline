"""
QUESTION:
Write a function named `generate_dice_outcomes` that generates all the possible outcomes of rolling a set of six-sided dice. The function should take the number of dice as an argument and return a list of tuples representing all possible outcomes. The function should work with any number of dice.
"""

def generate_dice_outcomes(n):
    """
    Generates all the possible outcomes of rolling a set of six-sided dice.

    Args:
        n (int): The number of dice.

    Returns:
        list: A list of tuples representing all possible outcomes.
    """
    return list(itertools.product(range(1, 7), repeat=n))