"""
QUESTION:
Write a function called `solve` that calculates the diagonal surface area of a 3-dimensional trapezohedron given its base width, top width, angle of inclination in degrees, and height. Assume the trapezohedron is a right trapezohedron with straight lateral edges. The angle should be converted from degrees to radians before calculation.
"""

import math

def solve(base_width, top_width, angle, height):
    """
    Calculate the diagonal surface area of a 3-dimensional trapezohedron.

    Parameters:
    base_width (float): The width of the base of the trapezohedron.
    top_width (float): The width of the top of the trapezohedron.
    angle (float): The angle of inclination in degrees.
    height (float): The height of the trapezohedron.

    Returns:
    float: The diagonal surface area of the trapezohedron.
    """
    angle_radians = math.radians(angle)
    diagonal_surface_area = 2 * (base_width + top_width) * height / math.tan(angle_radians/2)
    return diagonal_surface_area