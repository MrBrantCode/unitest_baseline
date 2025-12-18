"""
QUESTION:
Given the area of a larger shape and a maximum allowable circumference, implement a function `calculate_circumference` that calculates the circumference of a circle inscribed within the shape, ensuring it does not exceed the maximum allowable circumference. The function should take two parameters: `A`, the area of the larger shape, and `k`, the maximum allowable circumference.
"""

import math

def calculate_circumference(A, k):
    """
    Calculate the circumference of a circle inscribed within a shape.

    Args:
    A (float): The area of the larger shape.
    k (float): The maximum allowable circumference.

    Returns:
    float: The circumference of the circle.
    """
    # Calculate the radius of the circle
    r = math.sqrt(A / math.pi)
    # Calculate the circumference of the circle
    C = 2 * math.pi * r
    # Check if the circumference exceeds the maximum allowable circumference
    if C > k:
        C = k
    return C