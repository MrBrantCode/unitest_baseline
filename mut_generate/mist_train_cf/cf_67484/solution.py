"""
QUESTION:
Design a function `triangle_perimeter` that takes the lengths of three sides of a triangle as input and returns the perimeter. The function should only calculate the perimeter if all side lengths are greater than zero; otherwise, it should indicate an error.
"""

def triangle_perimeter(side1, side2, side3):
    """
    Calculate the perimeter of a triangle given the lengths of its sides.

    Args:
        side1 (float): The length of the first side.
        side2 (float): The length of the second side.
        side3 (float): The length of the third side.

    Returns:
        float: The perimeter of the triangle if all side lengths are greater than zero.
        str: An error message if any side length is not greater than zero.
    """
    if side1 > 0 and side2 > 0 and side3 > 0:
        return side1 + side2 + side3
    else:
        return "Error: Sides of a triangle should be greater than zero."