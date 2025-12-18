"""
QUESTION:
Write a function `triangle_area(side1, side2=None, side3=None)` that calculates the area of a triangle given its sides. The function should accept one, two, or three arguments. If one argument is provided, it is assumed to be the side of an equilateral triangle. If two arguments are provided, they are assumed to be the base and height of an isosceles triangle. If three arguments are provided, they are assumed to be the sides of a scalene triangle. The function should return the area of the triangle.
"""

import math
def triangle_area(side1, side2=None, side3=None):
    if side2 is None and side3 is None:
        area = (math.sqrt(3) / 4) * pow(side1, 2)
    elif side3 is None:
        area = 0.5 * side1 * side2
    else:
        semi_perimeter = (side1 + side2 + side3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    
    return area