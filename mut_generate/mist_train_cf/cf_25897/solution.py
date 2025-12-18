"""
QUESTION:
Write a function named `identify_triangle_type` that takes three integer sides of a triangle as input and returns the type of the triangle. The function should consider the following conditions: 
- If all three sides are equal, it's an equilateral triangle.
- If exactly two sides are equal, it's an isosceles triangle.
- If none of the sides are equal, it's a scalene triangle.
- If the sum of the lengths of any two sides is not greater than the length of the third side, it's not a valid triangle.
"""

def identify_triangle_type(a, b, c):
    """
    This function identifies the type of a triangle given its three sides.

    Args:
        a (int): The length of the first side.
        b (int): The length of the second side.
        c (int): The length of the third side.

    Returns:
        str: The type of the triangle (equilateral, isosceles, scalene, or not a valid triangle).
    """

    # Check if the given sides can form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a valid triangle"

    # Check if all sides are equal
    if a == b == c:
        return "equilateral"

    # Check if exactly two sides are equal
    elif a == b or a == c or b == c:
        return "isosceles"

    # If none of the above conditions are met, it's a scalene triangle
    else:
        return "scalene"