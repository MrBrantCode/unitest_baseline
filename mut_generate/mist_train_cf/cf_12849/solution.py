"""
QUESTION:
Write a function `calculate_area` that takes a list of integers representing the lengths of the sides of a shape as input and returns the area of the shape. The shape can have a maximum of 5 sides. Also, write a function `calculate_perimeter` that calculates the perimeter of the shape. The input list should contain at least 3 and at most 5 integers. If the input list contains an invalid number of sides, the `calculate_area` function should return None.
"""

import math

def calculate_area(sides):
    """
    Calculate the area of a shape with 3-5 sides.

    Args:
        sides (list): A list of integers representing the lengths of the sides of a shape.

    Returns:
        float: The area of the shape, or None if the input list contains an invalid number of sides.
    """
    if len(sides) == 3:  # Triangle
        a, b, c = sides
        s = (a + b + c) / 2  # Semiperimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    elif len(sides) == 4:  # Quadrilateral
        a, b, c, d = sides
        area = (a * b * c * d) ** 0.5
        return area
    elif len(sides) == 5:  # Pentagon
        a, b, c, d, e = sides
        area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (a ** 2)
        return area
    else:
        return None

def calculate_perimeter(sides):
    """
    Calculate the perimeter of a shape.

    Args:
        sides (list): A list of integers representing the lengths of the sides of a shape.

    Returns:
        int: The perimeter of the shape.
    """
    perimeter = sum(sides)
    return perimeter