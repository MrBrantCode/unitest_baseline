"""
QUESTION:
Write a function `triangle_area` that calculates the area of a triangle given the lengths of its three sides. The function should take three positive numbers as input and return the area of the corresponding triangle. The function should use Heron's formula: area = sqrt(s*(s-a)*(s-b)*(s-c)) where s is the semi-perimeter (s = (a + b + c) / 2) and a, b, c are the lengths of the sides.
"""

import math

def triangle_area(a, b, c):
    """
    Calculate the area of a triangle given the lengths of its three sides.

    Args:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.

    Returns:
        float: The area of the triangle.
    """
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area