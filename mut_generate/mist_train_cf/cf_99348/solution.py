"""
QUESTION:
Write a function `solve_quadratic_equation` that solves a quadratic equation of the form ax^2 + bx + c = 0, where a, b, and c are coefficients. The function should return the roots of the equation. The function should handle cases where the equation has one, two real roots, or two complex roots.
"""

import math

def solve_quadratic_equation(a, b, c):
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.

    Args:
        a (float): Coefficient of x^2
        b (float): Coefficient of x
        c (float): Constant term

    Returns:
        tuple: Roots of the equation
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
        return (real_part, imaginary_part, "i"), (real_part, -imaginary_part, "i")