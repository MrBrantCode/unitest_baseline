"""
QUESTION:
Write a function `area_circle` that calculates the area of a circle given a radius `r`. The function should take one argument `r`, a double-precision floating point number, and return the calculated area as a double-precision floating point number. The area should be calculated using the formula πr^2, approximated as 3.14*r*r.
"""

def area_circle(r: float) -> float:
    """
    Calculate the area of a circle given a radius r.

    Args:
    r (float): The radius of the circle.

    Returns:
    float: The calculated area of the circle.
    """
    return 3.14 * r * r