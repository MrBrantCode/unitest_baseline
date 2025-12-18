"""
QUESTION:
Implement a function `identify_quadrilateral(d, e, alpha, beta)` that takes as input the lengths of the diagonals (d and e) and the angles between these diagonals (α and β) in degrees, and returns the type of quadrilateral (square, rhombus, rectangle, or parallelogram). The function should assume that α and β are the acute and obtuse angles between the diagonals, and that the input values represent a valid quadrilateral.
"""

import math

def identify_quadrilateral(d, e, alpha, beta):
    # convert the angles from degrees to radians
    alpha = math.radians(alpha)
    beta = math.radians(beta)

    # check for a square
    if d == e and alpha == beta == math.pi/2:
        return 'Square'
    # check for a rhombus
    elif d == e and alpha != beta and abs(alpha-beta) == math.pi/2:
        return 'Rhombus'
    # check for a rectangle
    elif d != e and alpha == beta == math.pi/2:
        return 'Rectangle'
    # for any other cases return parallelogram
    else:
        return 'Parallelogram'