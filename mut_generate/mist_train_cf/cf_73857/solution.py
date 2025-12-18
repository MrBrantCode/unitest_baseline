"""
QUESTION:
Given the lengths of the diagonals of a kite, calculate the perimeter and the area of the kite. The function should be named `kite_properties` and should take two parameters: `d1` and `d2`, representing the lengths of the diagonals. The function should return the area and the perimeter of the kite. The perimeter should be calculated using the Pythagorean Theorem to find the length of each side, and the area should be calculated using the formula 1/2 * d1 * d2.
"""

import math

def kite_properties(d1, d2):
    """
    Calculate the perimeter and the area of a kite given the lengths of its diagonals.

    Parameters:
    d1 (float): The length of the first diagonal.
    d2 (float): The length of the second diagonal.

    Returns:
    tuple: A tuple containing the area and the perimeter of the kite.
    """
    # Calculate the area using the formula 1/2 * d1 * d2
    area = 0.5 * d1 * d2
    
    # Calculate the length of each side using the Pythagorean Theorem
    side_length = math.sqrt((0.5 * d1) ** 2 + (0.5 * d2) ** 2)
    
    # Calculate the perimeter by multiplying the side length by 4
    perimeter = 4 * side_length
    
    return area, perimeter