"""
QUESTION:
Write a function called `calculate_displacement` that takes in four parameters representing the east, north, west, and south distances traveled. Calculate the straight-line distance between the initial position and the final one after these movements. The function should return the final displacement. Assume all distances are in miles.
"""

import math

def calculate_displacement(east, north, west, south):
    """
    Calculate the straight-line distance between the initial position and the final one after movements.

    Args:
    east (float): Distance traveled east.
    north (float): Distance traveled north.
    west (float): Distance traveled west.
    south (float): Distance traveled south.

    Returns:
    float: The final displacement.
    """
    # Calculate the total eastward displacement
    east_displacement = east - west
    
    # Calculate the total northward displacement
    north_displacement = north - south
    
    # Calculate displacement from the initial point using Pythagorean theorem
    total_displacement = math.sqrt(east_displacement**2 + north_displacement**2)
    
    return total_displacement