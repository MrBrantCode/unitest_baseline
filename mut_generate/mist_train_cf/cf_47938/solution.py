"""
QUESTION:
Write a Python function named `solve_quadratic` that takes in three coefficients a, b, and c of a quadratic equation ax^2 + bx + c = 0, and returns the two roots of the equation. The function should work for both real and complex roots.
"""

import cmath

def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation ax^2 + bx + c = 0.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple: Two roots of the quadratic equation.
    """
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two possible solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    return sol1, sol2