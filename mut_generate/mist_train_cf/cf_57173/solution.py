"""
QUESTION:
Write a function `is_right_angled` that determines if a triangle with three given side lengths is a right-angled triangle. The function should take as input three integers representing the side lengths of the triangle and return `True` if the triangle is right-angled and `False` otherwise. The function should consider all possible combinations of side lengths to ensure accurate classification.
"""

def is_right_angled(a, b, c):
    """
    This function determines if a triangle with side lengths a, b, and c is a right-angled triangle.
    
    Parameters:
    a (int): The length of the first side of the triangle.
    b (int): The length of the second side of the triangle.
    c (int): The length of the third side of the triangle.
    
    Returns:
    bool: True if the triangle is right-angled, False otherwise.
    """

    # Sort the sides of the triangle in ascending order
    sides = sorted([a, b, c])
    
    # According to the Pythagorean theorem, the sum of the squares of the two shorter sides
    # should be equal to the square of the longest side in a right-angled triangle
    return sides[0]**2 + sides[1]**2 == sides[2]**2