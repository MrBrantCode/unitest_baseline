"""
QUESTION:
Write a Python function named `solve_quadratic_equation` to solve the quadratic equation `ax^2 + bx + c = 0` where `a`, `b`, and `c` are coefficients of the equation. The function should calculate the roots of the equation and return the numerical values of the roots. The function should handle cases where the equation has two real roots, one real root, or two complex roots.
"""

import math

def solve_quadratic_equation(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0 and returns the roots.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    tuple: Roots of the quadratic equation
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, negative or zero
    if discriminant > 0:
        # There are two real roots
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # There is one real root
        x = -b / (2*a)
        return x,
    else:
        # There are two complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)