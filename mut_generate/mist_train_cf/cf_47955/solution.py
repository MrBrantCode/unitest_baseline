"""
QUESTION:
Find the roots of a quadratic polynomial equation ax^2 + bx + c = 0. Implement a function named `find_roots` that takes the coefficients a, b, and c as inputs and returns the roots of the equation. The function should handle all possible cases of the discriminant (D = b^2 - 4ac), including real and distinct roots, real and equal roots, and complex and different roots.
"""

import math
import cmath

def find_roots(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c

    # Check the nature of the discriminant
    if D > 0:
        # Calculate real and distinct roots
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return root1, root2
    elif D == 0:
        # Calculate real and equal roots
        root = -b / (2 * a)
        return root, root
    else:
        # Calculate complex and different roots
        realPart = -b / (2 * a)
        imaginaryPart = math.sqrt(-D) / (2 * a)
        root1 = complex(realPart, imaginaryPart)
        root2 = complex(realPart, -imaginaryPart)
        return root1, root2