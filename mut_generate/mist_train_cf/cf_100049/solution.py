"""
QUESTION:
Write a function named `calculate_circumference` that calculates the circumference of a circle given the area of the larger shape and the maximum allowable circumference. The function should take two parameters, `A` (the area of the larger shape) and `k` (the maximum allowable circumference). The function should return the calculated circumference, ensuring it does not exceed the maximum allowable value.
"""

import math

def calculate_circumference(A, k):
    """
    Calculate the circumference of a circle given the area of the larger shape and the maximum allowable circumference.

    Parameters:
    A (float): Area of the larger shape.
    k (float): Maximum allowable circumference.

    Returns:
    float: Calculated circumference, not exceeding the maximum allowable value.
    """
    r = math.sqrt(A/math.pi)  # Radius of the circle
    C = 2*math.pi*r  # Circumference of the circle
    return min(C, k)  # Return the minimum value between C and k