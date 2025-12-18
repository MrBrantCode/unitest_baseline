"""
QUESTION:
Write a function `solve_quadratic_equation` that calculates the solutions to a quadratic equation of the form Ax² + Bx + C = 0, where A, B, and C are coefficients. The function should return the two solutions, handling both real and complex roots. The coefficients A, B, and C will be provided as input to the function.
"""

import cmath

def solve_quadratic_equation(A, B, C):
    """
    Calculates the solutions to a quadratic equation of the form Ax² + Bx + C = 0.

    Args:
        A (float): Coefficient of x²
        B (float): Coefficient of x
        C (float): Constant term

    Returns:
        tuple: Two solutions to the quadratic equation
    """

    # calculate the discriminant
    D = (B**2) - (4*A*C)

    # find two solutions
    sol1 = (-B-cmath.sqrt(D))/(2*A)
    sol2 = (-B+cmath.sqrt(D))/(2*A)

    return sol1, sol2