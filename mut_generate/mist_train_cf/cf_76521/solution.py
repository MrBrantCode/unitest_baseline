"""
QUESTION:
Write a function `calculate_ladder_length` that takes the angle and height as parameters and returns the length of the ladder. The angle is in degrees and the height is the distance from the ground where the ladder touches the wall. Use the sine function from trigonometry to calculate the length. The function should return the absolute length of the ladder.
"""

import math

def calculate_ladder_length(angle, height):
    """
    Calculate the length of the ladder given the angle and height.

    Parameters:
    angle (float): The angle in degrees.
    height (float): The height from the ground where the ladder touches the wall.

    Returns:
    float: The absolute length of the ladder.
    """
    # Convert angle from degrees to radians for math.sin() function
    angle_in_radians = math.radians(angle)
    
    # Calculate the length of the ladder using the sine function
    ladder_length = height / math.sin(angle_in_radians)
    
    # Return the absolute length of the ladder
    return abs(ladder_length)