"""
QUESTION:
Write a function `expected_rounds(n)` that calculates the expected number of rounds before the game concludes with `n` participants seated in a circular arrangement. The function should return the result rounded to the nearest integer. Assume `n` is an even number and is greater than 1.
"""

def expected_rounds(n):
    """
    Calculate the expected number of rounds before the game concludes 
    with n participants seated in a circular arrangement.

    Args:
    n (int): The number of participants. It should be an even number and greater than 1.

    Returns:
    int: The expected number of rounds before the game concludes.
    """
    return round((n**2 - 1) / 4)