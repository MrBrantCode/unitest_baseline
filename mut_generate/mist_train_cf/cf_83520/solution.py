"""
QUESTION:
Write a function `trapezoid_area` that calculates the area of an isosceles trapezoid. The function should take three arguments: `a` and `b` representing the lengths of the parallel sides, and `distance` representing the separation distance between the parallel sides. The area should be calculated using the formula: 1/2 * (a + b) * distance.
"""

def trapezoid_area(a, b, distance):
    """
    Calculate the area of an isosceles trapezoid.

    Args:
    a (float): The length of one parallel side.
    b (float): The length of the other parallel side.
    distance (float): The separation distance between the parallel sides.

    Returns:
    float: The area of the trapezoid.
    """
    return 0.5 * (a + b) * distance