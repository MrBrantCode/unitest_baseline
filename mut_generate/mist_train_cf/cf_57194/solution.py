"""
QUESTION:
Create a function `solve_quadratic(a, b, c)` that solves the quadratic equation `ax^2 + bx + c = 0` and returns its roots. The function should handle complex roots and represent them in standard form. It should be able to handle any coefficients, regardless of their size, while ensuring numerical stability and precision. The function assumes that `a` is non-zero (if `a` is zero, the equation is not quadratic) and does not handle cases where the denominator becomes zero.
"""

import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    # Calculate the two solutions
    sol1 = (-b - discriminant) / (2*a)
    sol2 = (-b + discriminant) / (2*a)
    
    return sol1, sol2