"""
QUESTION:
Calculate the area and inradius of a triangle given its side lengths A, B, and C using Heron's formula. The function should take three parameters, A, B, and C, representing the lengths of the sides of the triangle, and return the calculated area and inradius. The input values are positive real numbers, and the function should return a tuple containing the area and inradius.
"""

import math

def calculate_properties(a, b, c):
    """
    Calculate the area and inradius of a triangle given its side lengths A, B, and C using Heron's formula.

    Args:
    a (float): The length of side A of the triangle.
    b (float): The length of side B of the triangle.
    c (float): The length of side C of the triangle.

    Returns:
    tuple: A tuple containing the calculated area and inradius of the triangle.
    """
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # Calculate the inradius
    inradius = area / s
    # Return the calculated area and inradius
    return area, inradius