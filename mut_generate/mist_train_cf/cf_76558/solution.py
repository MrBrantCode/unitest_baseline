"""
QUESTION:
Write a function `calculate_quadrilateral_area` that calculates the area of a cyclic quadrilateral using Brahmagupta's formula. The function should take four sides a, b, c, and d as input and return the calculated area.
"""

import math

def calculate_quadrilateral_area(a, b, c, d):
    """
    Calculate the area of a cyclic quadrilateral using Brahmagupta's formula.

    Args:
        a (float): Length of the first side.
        b (float): Length of the second side.
        c (float): Length of the third side.
        d (float): Length of the fourth side.

    Returns:
        float: The calculated area of the quadrilateral.
    """

    # Calculate the semiperimeter of the quadrilateral
    s = (a + b + c + d) / 2

    # Apply Brahmagupta's formula to calculate the area
    area = math.sqrt((s - a) * (s - b) * (s - c) * (s - d))

    return area