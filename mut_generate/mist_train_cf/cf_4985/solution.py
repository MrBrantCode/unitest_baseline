"""
QUESTION:
Write a function named `calculate_triangle_area` that takes three parameters `a`, `b`, and `c` representing the lengths of a triangle's sides. The function should return the area of the triangle using Heron's formula if the given side lengths form a valid triangle, and return a message indicating that the side lengths do not form a valid triangle otherwise. The function should assume that the input values of `a`, `b`, and `c` are within the range of 1 to 100.
"""

def calculate_triangle_area(a, b, c):
    """
    Calculate the area of a triangle given its side lengths.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        float or str: The area of the triangle if the given side lengths form a valid triangle, 
                      otherwise a message indicating that the side lengths do not form a valid triangle.
    """
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
    else:
        return "The given side lengths do not form a valid triangle."