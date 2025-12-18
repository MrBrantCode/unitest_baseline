"""
QUESTION:
Write a function `circle_square_area_difference` that calculates the difference in area between a square inscribed in a circle and a square circumscribed by the same circle, given that the circle has a radius of 10 cm.
"""

import math

def circle_square_area_difference(radius):
    """
    Calculate the difference in area between a square inscribed in a circle and a square circumscribed by the same circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The difference in area between the two squares.
    """

    # Calculate the side of the inscribed square
    inscribed_square_side = 2 * radius

    # Calculate the area of the inscribed square
    inscribed_square_area = inscribed_square_side ** 2

    # Calculate the side of the circumscribed square
    circumscribed_square_side = (2 * radius) / math.sqrt(2)

    # Calculate the area of the circumscribed square
    circumscribed_square_area = circumscribed_square_side ** 2

    # Calculate the difference in area between the two squares
    area_difference = inscribed_square_area - circumscribed_square_area

    return area_difference