"""
QUESTION:
Write a function named `calculate_hypotenuse_and_area` that takes the base and height of a right triangle as input. The function should calculate and return the length of the hypotenuse using the Pythagorean theorem and the area of the triangle.
"""

import math

def calculate_hypotenuse_and_area(base, height):
    """
    This function calculates the length of the hypotenuse and area of a right triangle.

    Args:
        base (float): The base of the right triangle.
        height (float): The height of the right triangle.

    Returns:
        tuple: A tuple containing the length of the hypotenuse and the area of the triangle.
    """
    hypotenuse = math.sqrt(base**2 + height**2)
    area = 0.5 * base * height
    return hypotenuse, area