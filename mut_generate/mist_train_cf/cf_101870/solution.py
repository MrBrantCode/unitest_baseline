"""
QUESTION:
Implement a function `calculate_circumference` that calculates the circumference of a circle within a larger shape, given the area of the larger shape (`A`) and the maximum allowable circumference (`k`). The function should return the final value of the circumference of the circle, ensuring that it does not exceed `k`.
"""

import math

def calculate_circumference(A, k):
    """
    Calculate the circumference of a circle within a larger shape.

    Parameters:
    A (float): Area of the larger shape
    k (float): Maximum allowable circumference

    Returns:
    float: The final value of the circumference of the circle
    """
    r = math.sqrt(A/math.pi) # Radius of the circle
    C = 2*math.pi*r # Circumference of the circle
    if C > k:
        C = k
    return C