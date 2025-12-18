"""
QUESTION:
Write a function `calculate_quadratic_roots` that takes the coefficients of a quadratic equation (a, b, c) as input and returns its roots.
"""

import cmath

def calculate_quadratic_roots(a, b, c):
    """
    Calculate the roots of a quadratic equation given its coefficients.

    Args:
    a (float): Coefficient of the quadratic term.
    b (float): Coefficient of the linear term.
    c (float): Constant term.

    Returns:
    tuple: The roots of the quadratic equation.
    """

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate the roots using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    return root1, root2