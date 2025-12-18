"""
QUESTION:
Write a function `quadratic_roots(a, b, c)` that calculates the roots of a second-degree polynomial equation `ax^2 + bx + c = 0`. The function should return the roots as a tuple. Consider the cases where the roots are real and distinct, real and equal, or complex.
"""

import math
import cmath

def quadratic_roots(a, b, c):
    
    # calculating the discriminant part
    disc = (math.pow(b, 2)) - (4 * a * c)

    # calculating real and complex roots
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2 * a)
        root2 = (-b - math.sqrt(disc)) / (2 * a)
    elif disc == 0:
        root1 = root2 = -b / (2 * a)
    else:
        root1 = (-b + cmath.sqrt(disc)) / (2 * a)
        root2 = (-b - cmath.sqrt(disc)) / (2 * a)
    
    return root1, root2