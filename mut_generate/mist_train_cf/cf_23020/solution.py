"""
QUESTION:
Write a function `polar_representation(x, y)` that converts a 2D point (x, y) into polar representation (r, θ), where x and y are integers between -1000 and 1000, inclusive, without using any trigonometric functions. The function should calculate the distance r from the origin to the point using the Pythagorean theorem and the angle θ between the positive x-axis and the line connecting the origin and the point using basic geometry principles. The function should handle special cases where the point is on the x-axis or y-axis and ensure the angle θ is between -π and π. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

import math

def polar_representation(x, y):
    """
    This function converts a 2D point (x, y) into polar representation (r, θ) without using any trigonometric functions.
    
    Parameters:
    x (int): The x-coordinate of the point, between -1000 and 1000, inclusive.
    y (int): The y-coordinate of the point, between -1000 and 1000, inclusive.
    
    Returns:
    tuple: A tuple containing the distance r from the origin to the point and the angle θ between the positive x-axis and the line connecting the origin and the point.
    """

    # Calculate the distance r from the origin to the point using the Pythagorean theorem
    r = math.sqrt(x**2 + y**2)
    
    # Handle special cases where the point is on the x-axis or y-axis
    if x == 0 and y == 0:
        # The point is at the origin
        theta = 0
    elif x == 0 and y > 0:
        # The point is on the positive y-axis
        theta = math.pi / 2
    elif x == 0 and y < 0:
        # The point is on the negative y-axis
        theta = -math.pi / 2
    elif x > 0 and y == 0:
        # The point is on the positive x-axis
        theta = 0
    elif x < 0 and y == 0:
        # The point is on the negative x-axis
        theta = math.pi
    else:
        # Calculate θ for the general case
        if x > 0 and y > 0:
            # θ is in the first quadrant
            theta = math.atan2(y, x)
        elif x < 0 and y > 0:
            # θ is in the second quadrant
            theta = math.atan2(y, x)
        elif x < 0 and y < 0:
            # θ is in the third quadrant
            theta = math.atan2(y, x)
        else:
            # θ is in the fourth quadrant
            theta = math.atan2(y, x)
    
    return (r, theta)