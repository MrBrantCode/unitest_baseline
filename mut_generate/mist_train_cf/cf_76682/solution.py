"""
QUESTION:
Write a function `calculate_combinations(total_marbles, red_blue_green, select_marbles)` to calculate the number of combinations that can be constructed by selecting a certain number of marbles, given that exactly one of the selected marbles must be specifically red, green, or blue. The function should take three parameters: `total_marbles` (the total number of marbles), `red_blue_green` (the number of red, green, and blue marbles), and `select_marbles` (the number of marbles to select). The function should return the total number of combinations.
"""

from math import comb

def calculate_combinations(total_marbles, red_blue_green, select_marbles):
    """
    Calculate the number of combinations that can be constructed by selecting a certain number of marbles,
    given that exactly one of the selected marbles must be specifically red, green, or blue.

    Args:
        total_marbles (int): The total number of marbles.
        red_blue_green (int): The number of red, green, and blue marbles.
        select_marbles (int): The number of marbles to select.

    Returns:
        int: The total number of combinations.
    """

    # Calculate the number of unspecified color marbles
    other_marbles = total_marbles - red_blue_green

    # Calculate the combinations of other marbles and red, green, blue marbles
    total_combinations = comb(other_marbles, select_marbles - 1) * comb(red_blue_green, 1)

    return total_combinations