"""
QUESTION:
Write a function `quadrilateral_type_and_area` that takes four arguments p, q, r, and s, representing the side lengths of a quadrilateral. The function should return a string representing the type of quadrilateral (rectangle, rhombus, square, parallelogram, trapezoid, or kite) and the area of the quadrilateral if possible, or a message stating that the area cannot be determined without additional information. Assume the quadrilateral can be either of the given types. The function should work for any valid combination of side lengths.
"""

import math

def quadrilateral_type_and_area(p, q, r, s):
    if p==q==r==s:
        quad_type = 'Square'
        area = p**2
    elif p==q and r==s:
        quad_type = 'Rectangle'
        diagonal = math.sqrt(p**2 + r**2)
        area = 0.5 * diagonal ** 2
    elif p==r and q==s:
        quad_type = 'Rhombus'
        area = 'Cannot determine without an angle'
    elif p==s and q==r:
        quad_type = 'Parallelogram'
        area = 'Cannot determine without an angle'
    else:
        quad_type = 'Trapezoid or Kite'
        area = 'Cannot determine without additional information'
    
    return quad_type, area