"""
QUESTION:
Create a function `calculate_triangle_perimeter(a, b, c)` that calculates the perimeter of a triangle given its three side lengths `a`, `b`, and `c`. The function should only accept integer side lengths greater than 0. It must validate if the given side lengths form a valid triangle, where the sum of any two side lengths is greater than the third side length. If the side lengths do not form a valid triangle, the function should return -1.
"""

def calculate_triangle_perimeter(a, b, c):
    """
    Calculate the perimeter of a triangle given its three side lengths.

    Args:
        a (int): The length of the first side.
        b (int): The length of the second side.
        c (int): The length of the third side.

    Returns:
        int: The perimeter of the triangle if the side lengths are valid; otherwise, -1.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    else:
        return -1