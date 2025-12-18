"""
QUESTION:
Write a function named `trapezoid_area` that calculates the surface area of an isosceles trapezoid. The function should take the lengths of the two parallel sides (`b1` and `b2`) and the perpendicular distance between them (`h`) as parameters. The function should return the surface area of the trapezoid using the formula A = [(b1 + b2)/2] * h.
"""

def trapezoid_area(b1, b2, h):
    """
    Calculate the surface area of an isosceles trapezoid.
    
    Parameters:
    b1 (float): The length of the first parallel side.
    b2 (float): The length of the second parallel side.
    h (float): The perpendicular distance between the parallel sides.
    
    Returns:
    float: The surface area of the trapezoid.
    """
    return (b1 + b2) / 2 * h