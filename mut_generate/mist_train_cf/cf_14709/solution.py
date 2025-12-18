"""
QUESTION:
Create a function called calculate_parallelogram_area that calculates the area of a parallelogram. The function should take two parameters, base and height, and return the calculated area. Note that the area can be negative if the height is negative, indicating that the height and base are on opposite sides of the parallelogram's center.
"""

def calculate_parallelogram_area(base, height):
    """
    Calculate the area of a parallelogram.

    Args:
        base (float): The base length of the parallelogram.
        height (float): The height of the parallelogram.

    Returns:
        float: The calculated area of the parallelogram.
    """
    return base * height