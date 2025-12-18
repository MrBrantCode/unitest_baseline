"""
QUESTION:
Create a function named "calculateArea" that takes the width and height of a rectangle as arguments and returns the area. The area is calculated by summing the width and height, then multiplying the result by 2. The function should be called with user-provided width and height values, which must be positive integers greater than 0.
"""

def calculateArea(width, height):
    """
    Calculate the area of a rectangle by summing the width and height, 
    then multiplying the result by 2.

    Args:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Returns:
    int: The calculated area of the rectangle.
    """
    area = (width + height) * 2
    return area