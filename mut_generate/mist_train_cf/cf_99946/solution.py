"""
QUESTION:
Implement the `calculate_circumference` function that takes two parameters, `max_circumference` and `area`, and returns the circumference of a circle. The circle's circumference must not exceed `max_circumference` and is part of a larger shape with `area`. Assume the area of the circle is equal to the area of the larger shape. Use the mathematical constant pi (π) approximately equal to 3.14 for the calculations.
"""

import math

def calculate_circumference(max_circumference, area):
    """
    Calculate the circumference of a circle that does not exceed max_circumference
    and is part of a larger shape with the given area.

    Args:
    max_circumference (float): The maximum allowable circumference of the circle.
    area (float): The area of the larger shape.

    Returns:
    float: The calculated circumference of the circle.
    """
    radius = math.sqrt(area/math.pi)
    circumference = 2*math.pi*radius
    if circumference > max_circumference:
        return max_circumference
    else:
        return circumference