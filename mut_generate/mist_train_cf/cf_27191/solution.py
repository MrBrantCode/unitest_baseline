"""
QUESTION:
Write a function `triangle_type` that takes three side lengths of a triangle as input and returns the type of the triangle if the sides form a valid triangle. The function should return one of the following types: 'equilateral', 'isosceles', or 'scalene'. If the sides do not form a valid triangle, the function should return 'invalid'. A valid triangle is one where the sum of the lengths of any two sides is greater than the length of the third side.
"""

def triangle_type(side1, side2, side3):
    """
    This function determines the type of triangle based on side lengths.
    
    Parameters:
    side1 (float): The length of the first side.
    side2 (float): The length of the second side.
    side3 (float): The length of the third side.
    
    Returns:
    str: The type of the triangle ('equilateral', 'isosceles', 'scalene', or 'invalid').
    """
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        if side1 == side2 == side3:
            return 'equilateral'
        elif side1 != side2 and side2 != side3 and side3 != side1:
            return 'scalene'
        else:
            return 'isosceles'
    else:
        return 'invalid'