"""
QUESTION:
Write a function named `trapezoid_area` that calculates the area of a trapezoid given the lengths of its parallel sides and the distance between them. The function should take three parameters: the lengths of the two parallel sides and the distance between them, and return the area of the trapezoid.
"""

def trapezoid_area(a, b, h):
    """
    Calculate the area of a trapezoid given the lengths of its parallel sides and the distance between them.

    Parameters:
    a (float): The length of the first parallel side.
    b (float): The length of the second parallel side.
    h (float): The distance between the parallel sides.

    Returns:
    float: The area of the trapezoid.
    """
    return 0.5 * (a + b) * h