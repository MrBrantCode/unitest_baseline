"""
QUESTION:
Create a function `rectangle_properties(a, b, c, d, e)` that calculates the area, type (square or rectangle), length of diagonals, and angle between diagonals of a rectangle. The function should validate if the lengths of the sides can produce a valid rectangle, where opposite sides are equal and all angles are 90 degrees. The lengths of the sides are given by `a`, `b`, `c`, `d` and the length of the diagonal is given by `e`. The function should return a tuple `(Area, Type, Length of Diagonals, Angle between Diagonals)` to 2 decimal points accuracy. If the rectangle is not valid, return -1.
"""

import math

def rectangle_properties(a, b, c, d, e):
    sides = sorted([a, b, c, d])
    
    # validation
    if (sides[0] == sides[1] and sides[2] == sides[3]) == False or round(math.pow(sides[0], 2) + math.pow(sides[2], 2), 2) != math.pow(e, 2):
        return -1
    else:
        Area = round( sides[0] * sides[2], 2)
        if sides[0] == sides[2]:
            Type = 'Square'
        else:
            Type = 'Rectangle'
        Diagonal = round(e, 2)
        Angle = 90
        return (Area, Type, Diagonal, Angle)