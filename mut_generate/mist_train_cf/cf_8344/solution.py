"""
QUESTION:
Calculate the volume of a cylinder using the formula V = πr²h, given the radius and height. The function should take two arguments: the radius and the height, and use the approximation value of π as 3.14159.
"""

def cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder using the formula V = πr²h.

    Args:
    radius (float): The radius of the cylinder.
    height (float): The height of the cylinder.

    Returns:
    float: The volume of the cylinder.
    """
    pi = 3.14159
    return pi * (radius ** 2) * height