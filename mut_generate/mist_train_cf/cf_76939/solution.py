"""
QUESTION:
Create a function called `calculate_width_reduction` that calculates the reduction in the horizontal breadth measurement of a television screen if a given diagonal measurement is used instead of the conventional horizontal length. The ratio of the length to the height of the television screen is 5:3 and the given measurement is 48 inches. The function should return the reduction amount rounded to the nearest inch.
"""

from math import sqrt

def calculate_width_reduction(diagonal_measurement, ratio_width_to_height):
    """
    Calculate the reduction in the horizontal breadth measurement of a television screen 
    if a given diagonal measurement is used instead of the conventional horizontal length.

    Args:
        diagonal_measurement (float): The diagonal measurement of the television screen.
        ratio_width_to_height (float): The ratio of the width to the height of the television screen.

    Returns:
        int: The reduction in width rounded to the nearest inch.
    """

    # Calculate the width using the given diagonal measurement
    new_width = (5 / sqrt(5**2 + 3**2)) * diagonal_measurement

    # Calculate the width if the given measurement is the horizontal length
    initial_width = diagonal_measurement

    # Calculate the amount by which the width would reduce
    reduce_amount = initial_width - new_width

    # Return the reduction amount rounded to the nearest inch
    return round(reduce_amount)