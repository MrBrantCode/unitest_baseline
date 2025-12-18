"""
QUESTION:
Calculate the area of a triangle given the lengths of its three sides using the Law of Cosines and the sine function. Implement a function called `calculate_triangle_area` that takes three parameters `a`, `b`, and `c`, which represent the lengths of the three sides of the triangle as floating-point numbers, and returns the area of the triangle.
"""

import math

def calculate_triangle_area(a, b, c):
    """
    Calculate the area of a triangle given the lengths of its three sides.

    Args:
    a (float): The length of side a.
    b (float): The length of side b.
    c (float): The length of side c.

    Returns:
    float: The area of the triangle.
    """

    # Check if the given sides can form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return 0.0
    
    # Use the Law of Cosines to find one of the angles of the triangle
    angle_a = math.acos((b**2 + c**2 - a**2) / (2 * b * c))

    # Use the sine function to find the area of the triangle
    area = 0.5 * b * c * math.sin(angle_a)
    
    return area