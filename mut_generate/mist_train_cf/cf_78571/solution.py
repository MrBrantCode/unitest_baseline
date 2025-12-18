"""
QUESTION:
Write a function `rhombus_area` that calculates the area of a rhombus given the lengths of its diagonals and the angle between them. The function should take three parameters: `d1` (the length of diagonal 1), `d2` (the length of diagonal 2), and `angle` (the angle between the diagonals in degrees). The function should return the area of the rhombus rounded to the nearest hundredth of a unit.
"""

import math

def rhombus_area(d1, d2, angle):
    """
    Calculate the area of a rhombus given the lengths of its diagonals and the angle between them.

    Parameters:
    d1 (float): The length of diagonal 1.
    d2 (float): The length of diagonal 2.
    angle (float): The angle between the diagonals in degrees.

    Returns:
    float: The area of the rhombus rounded to the nearest hundredth of a unit.
    """
    return round((d1 * d2 * math.sin(math.radians(angle))) / 2, 2)