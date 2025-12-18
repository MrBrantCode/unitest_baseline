"""
QUESTION:
Create a function `calculate_triangle_area` that takes two parameters, `base` and `height`, representing the base and height of a triangle in centimeters, respectively. The function should calculate and return the area of the triangle. Assume the inputs are non-negative integers.
"""

def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Args:
        base (int): The base of the triangle in centimeters.
        height (int): The height of the triangle in centimeters.

    Returns:
        float: The area of the triangle in square centimeters.
    """
    return (base * height) / 2