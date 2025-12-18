"""
QUESTION:
Write a function named `find_roots` that takes three distinct numerical coefficients a, b, and c as input and returns the roots of a quadratic function ax^2 + bx + c, handling both real and complex roots.
"""

import cmath

def find_roots(a, b, c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2*a)
    sol2 = (-b + cmath.sqrt(d)) / (2*a)

    return sol1, sol2