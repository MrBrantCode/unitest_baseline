"""
QUESTION:
Write a function `compute_roots(a, b, c)` that calculates the roots of a complex quadratic equation of the form `ax^2 + bx + c = 0`. The function should handle complex roots and edge cases where the equation has one root, two equal roots, or no real roots.
"""

import cmath

def compute_roots(a, b, c):
    # correct equation for calculating the roots
    root1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    root2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a)
    
    return root1, root2