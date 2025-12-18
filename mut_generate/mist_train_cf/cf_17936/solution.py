"""
QUESTION:
Create a function called "calculateArea" that takes two arguments: width and height, both of which are integers. The function should calculate the area of a rectangle by summing up the width and height, then multiplying the result by 2, and return the calculated area. The width and height should be positive integers greater than 0 and less than or equal to 1000. If the input values are not valid, display an error message and ask for the input again. The calculated area should be rounded to the nearest whole number.
"""

def calculateArea(width, height):
    """
    Calculate the area of a rectangle by summing up the width and height, 
    then multiplying the result by 2, and return the calculated area.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Returns:
        int: The calculated area of the rectangle.
    """
    area = round((width + height) * 2)
    return area