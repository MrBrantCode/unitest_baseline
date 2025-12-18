"""
QUESTION:
Write a function `triangle_type` that determines the type of triangle given the lengths of its three sides. The sides are positive integers and must satisfy the triangle inequality theorem. The function should return a string indicating the type of triangle: 'equilateral', 'isosceles', 'scalene', or 'degenerate'.
"""

def triangle_type(a, b, c):
    """
    Determine the type of triangle given the lengths of its three sides.

    Args:
        a (int): The length of the first side.
        b (int): The length of the second side.
        c (int): The length of the third side.

    Returns:
        str: A string indicating the type of triangle: 'equilateral', 'isosceles', 'scalene', or 'degenerate'.
    """

    # Sort the sides in ascending order to simplify the comparison
    a, b, c = sorted([a, b, c])

    # Check if the sides satisfy the triangle inequality theorem
    if a + b <= c:
        return 'degenerate'
    elif a == b == c:
        return 'equilateral'
    elif a == b or b == c:
        return 'isosceles'
    else:
        return 'scalene'