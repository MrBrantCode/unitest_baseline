"""
QUESTION:
Write a function called `calculate_triangle_area` that takes the length of the hypotenuse and an angle of a right triangle as input, calculates the area of the triangle in square inches using trigonometric properties, and returns the result. The input angle is given in degrees and the function should handle the conversion to radians. The function should not take any other parameters.
"""

import math

def calculate_triangle_area(hypotenuse, angle):
    """
    Calculate the area of a right triangle using trigonometric properties.

    Args:
        hypotenuse (float): The length of the hypotenuse in inches.
        angle (float): The angle of the right triangle in degrees.

    Returns:
        float: The area of the triangle in square inches.
    """
    # calculate the length of the legs
    leg_length = math.sin(math.radians(angle)) * hypotenuse

    # calculate the area
    area = 0.5 * leg_length * leg_length

    return area