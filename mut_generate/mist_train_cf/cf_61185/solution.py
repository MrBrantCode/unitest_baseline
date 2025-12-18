"""
QUESTION:
Write a function `trapezoid_properties` that calculates the area and perimeter of a trapezoid given the lengths of its parallel sides (a and b), the length of the slant height (c), and the length of the height (h) if known. If the height is unknown, the function should calculate it using the Pythagorean theorem, assuming the trapezoid is either isosceles or right-angled. The function should return the calculated area and perimeter. The input values should be non-negative numbers, and 'a' should be less than or equal to 'b'.
"""

import math

def trapezoid_properties(base1, base2, slant_height, height=None):
    """
    Calculate the area and perimeter of a trapezoid.

    Args:
    base1 (float): The length of the first parallel side.
    base2 (float): The length of the second parallel side.
    slant_height (float): The length of the slant height.
    height (float, optional): The length of the height. Defaults to None.

    Returns:
    tuple: A tuple containing the area and perimeter of the trapezoid.
    """
    if height is None:
        if base1 == base2:  # If the trapezoid is regular or isosceles
            height = math.sqrt(slant_height ** 2 - ((base2 - base1) / 2) ** 2)
        else:  # If the trapezoid is right-angled
            height = math.sqrt(slant_height ** 2 - (base2 - base1) ** 2)

    area = (base1 + base2) * height / 2
    perimeter = base1 + base2 + 2 * slant_height

    return area, perimeter