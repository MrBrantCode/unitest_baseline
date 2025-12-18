"""
QUESTION:
Create a function `triangle_area` that calculates the area of a triangle using bitwise operations. The base and height of the triangle are given as integers. The function should take two integers as input, the base and the height, and return the area of the triangle. The area calculation should be performed using only bitwise operations, with the result being an integer representing the area.
"""

def triangle_area(base, height):
    """
    Calculate the area of a triangle using bitwise operations.

    Args:
        base (int): The base of the triangle.
        height (int): The height of the triangle.

    Returns:
        int: The area of the triangle.
    """
    # Calculate the product of the base and height
    product = base * height
    
    # Use bitwise right shift operation to divide the product by 2
    area = product >> 1
    
    return area