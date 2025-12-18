"""
QUESTION:
Write a Python function `calculate_shape_properties` that takes a list of sides of a shape (with a maximum of 5 sides) as input and returns a tuple containing the area and perimeter of the shape. Assume that all shapes are regular (all sides are equal) and that the input list will not be empty. Use mathematical formulas to calculate the area and perimeter.
"""

import math

def calculate_shape_properties(sides):
    if len(sides) == 3:  # Triangle
        a, b, c = sides
        s = (a + b + c) / 2  # Semiperimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    elif len(sides) == 4:  # Quadrilateral
        a, b, c, d = sides
        area = (a * b * c * d) ** 0.5
    elif len(sides) == 5:  # Pentagon
        a, b, c, d, e = sides
        area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (a ** 2)
    else:
        return None

    perimeter = sum(sides)
    return (area, perimeter)