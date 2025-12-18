"""
QUESTION:
Calculate the area of a parallelogram given its base length and angle of height. The function should be named parallelogram_area, take the base length and angle in degrees as arguments, and return the calculated area. The base length and angle are provided, with the base length given in centimeters and the angle in degrees.
"""

import math

def parallelogram_area(base_length, angle):
    """
    Calculate the area of a parallelogram given its base length and angle of height.

    Args:
        base_length (float): The base length of the parallelogram in centimeters.
        angle (float): The angle of height in degrees.

    Returns:
        float: The calculated area of the parallelogram in square centimeters.
    """
    # Convert the angle from degrees to radians for math.sin function
    angle_in_radians = math.radians(angle)
    
    # Calculate the height using the formula base_length * sin(angle)
    height = base_length * math.sin(angle_in_radians)
    
    # Calculate the area as the product of base length and height
    area = base_length * height
    
    return area