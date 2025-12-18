"""
QUESTION:
Write a function `quadratic_roots(a, b, c)` that takes the coefficients `a`, `b`, and `c` of a quadratic equation as input and returns the two roots of the equation, which can be real or complex numbers. The function should use the quadratic formula `x = [-b ± sqrt(b^2 - 4ac)] / 2a` to calculate the roots.
"""

import cmath

def quadratic_roots(a, b, c):
    """
    Calculate the roots of a quadratic equation given its coefficients a, b, and c.

    Args:
        a (float): Coefficient of the quadratic term.
        b (float): Coefficient of the linear term.
        c (float): Constant term.

    Returns:
        tuple: The two roots of the quadratic equation.
    """
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    return sol1, sol2