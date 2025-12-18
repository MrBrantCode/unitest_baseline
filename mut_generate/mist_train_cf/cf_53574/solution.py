"""
QUESTION:
Write a function `diamond_properties` that takes the lengths of the diagonals `d1` and `d2` of a diamond and an acute angle `theta` in degrees as input and returns the area of the diamond and the length of its sides. The diamond is assumed to be a rhombus.
"""

import math

def diamond_properties(d1, d2, theta):
    """
    Calculate the area of a diamond and the length of its sides.
    
    Parameters:
    d1 (float): The length of the first diagonal.
    d2 (float): The length of the second diagonal.
    theta (float): The acute angle in degrees.
    
    Returns:
    tuple: A tuple containing the area of the diamond and the length of its side.
    """
    # Convert theta to radians for use with math.cos
    theta_rad = math.radians(theta)
    
    # Calculate the area of the diamond
    area = 0.5 * d1 * d2
    
    # Calculate the length of the side using the Law of Cosines
    side_length = math.sqrt((d1**2 + d2**2 - 2*d1*d2*math.cos(theta_rad))/4)
    
    return area, side_length