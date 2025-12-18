"""
QUESTION:
Write a function `calculate_triangle_area` that takes three string inputs representing the sides of a triangle and returns the area of the triangle. The function should convert the string inputs to integers, calculate the semi-perimeter using the converted integers, and then calculate the area using Heron's formula.
"""

import math

def calculate_triangle_area(side1, side2, side3):
    """
    Calculate the area of a triangle given the lengths of its three sides.

    Args:
        side1 (str): The length of the first side.
        side2 (str): The length of the second side.
        side3 (str): The length of the third side.

    Returns:
        float: The area of the triangle.
    """
    # Convert string inputs to integers
    side1 = int(side1)
    side2 = int(side2)
    side3 = int(side3)

    # Calculate the semi-perimeter
    s = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    return area