"""
QUESTION:
Design a function `rectangle_properties(a, b, c, d, e)` that calculates the properties of a rectangle or square given the lengths of its sides `a`, `b`, `c`, `d`, and the length of one of its diagonals `e`. 

The function should verify if the declared lengths of the sides can form a valid quadrilateral by checking if opposing sides are identical and each angle measures 90 degrees, and if the length of the diagonal is consistent with the Pythagorean theorem. 

If the quadrilateral is valid, the function should return a tuple containing the area, type ('Square' or 'Rectangle'), length of the diagonals, and angle between the diagonals (which is always 90 degrees). If the quadrilateral does not pass verification, the function should return -1.
"""

import math

def rectangle_properties(a, b, c, d, e):
    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return -1

    if a != c or b != d or a*a + b*b != e*e:
        return -1

    p = math.sqrt(pow(c, 2) + pow(d, 2))

    if p != e:
        return -1
    
    # Check if the quadrilateral is square or rectangle
    if a == b:
        name = 'Square'
    else:
        name = 'Rectangle'

    # Calculate area
    area = a * b

    # Calculate diagonals
    diagonals = e

    # The angle between diagonals in a rectangle is always 90 degrees
    angle = 90

    return (round(area, 2), name, round(diagonals, 2), angle)