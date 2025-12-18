"""
QUESTION:
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
"""

def can_form_triangle(a: int, b: int, c: int) -> bool:
    """
    Determines if a triangle can be formed with the given side lengths.

    Parameters:
    a (int): The length of the first side.
    b (int): The length of the second side.
    c (int): The length of the third side.

    Returns:
    bool: True if a triangle can be formed, False otherwise.
    """
    return a + b > c and a + c > b and b + c > a