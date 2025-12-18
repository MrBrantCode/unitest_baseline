"""
QUESTION:
Determine the length of each diagonal of a rhomboid given its surface area (150 square units) and the relationship between the diagonals (d2 = 2d1), where d1 and d2 are the lengths of the diagonals. Write a function `find_diagonals` to solve for d1 and d2 using the formula A = 0.5 * d1 * d2.
"""

import math

def find_diagonals(area):
    """
    Calculate the lengths of the diagonals of a rhomboid.

    Args:
        area (float): The surface area of the rhomboid.

    Returns:
        tuple: A tuple containing the lengths of the diagonals (d1, d2).
    """
    d1 = math.sqrt(area)
    d2 = 2 * d1
    return d1, d2