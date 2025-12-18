"""
QUESTION:
Create a function named 'hexagon_properties' that takes the side length of a regular hexagon as an argument and returns the area and perimeter of the hexagon. The area should be calculated using the formula A = (3 * sqrt(3) * side^2) / 2 and the perimeter should be calculated using the formula P = 6 * side.
"""

import math

def hexagon_properties(side):
    """
    Calculate the area and perimeter of a regular hexagon.
    
    Parameters:
    side (float): The length of a side of the hexagon.
    
    Returns:
    tuple: A tuple containing the area and perimeter of the hexagon.
    """
    area = (3 * math.sqrt(3) * side**2) / 2
    perimeter = 6 * side
    return area, perimeter