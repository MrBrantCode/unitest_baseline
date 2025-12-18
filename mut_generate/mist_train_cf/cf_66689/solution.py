"""
QUESTION:
Write a function `quadrilateral_type(p, q, r, s, d1, d2)` that determines the type of quadrilateral represented by the 4 sides of lengths `p`, `q`, `r`, and `s`, and the two diagonals of lengths `d1` and `d2`. The function should return one of the following types: square, rectangle, parallelogram, rhombus, kite, trapezoid, or ordinary quadrilateral. The function should use the Pythagorean theorem or geometric properties of special quadrilaterals as needed.
"""

import math

def quadrilateral_type(p, q, r, s, d1, d2):
    if p == q == r == s:
        if d1 == d2:
            # All sides are equal and diagonals are equal - It's a square
            return 'Square'
        else:
            # All sides are equal but diagonals are not - It's a rhombus
            return 'Rhombus'
    elif p==q and r==s:
        if math.sqrt(p**2 + r**2) == d1 or math.sqrt(p**2 + r**2) == d2:
            # Opposite sides are equal and diagonals are perpendicular - It's a rectangle
            return 'Rectangle'
        else:
            # Opposite sides are equal -  It's a parallelogram 
            return 'Parallelogram'
    elif p==r and q==s and d1 != d2 : 
       # Adjacent sides are equal but diagonals are not - It's a Kite
       return 'Kite'
    else:
        # If none of the above conditions are met - It's an ordinary quadrilateral
        return 'Ordinary Quadrilateral'