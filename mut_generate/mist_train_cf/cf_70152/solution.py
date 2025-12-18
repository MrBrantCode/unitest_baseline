"""
QUESTION:
Develop a function, `solve_quadratic`, that determines the solution(s) of a quadratic equation of the form ax² + bx + c = 0 for the variable x. The function should take three parameters, a, b, and c, representing the coefficients of x², x, and the constant term, respectively. The function should return the solution(s) to the equation, handling cases where the equation has zero, one, or two real solutions.
"""

import math

def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation of the form ax² + bx + c = 0.

    Args:
        a (float): Coefficient of x².
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        list: Solutions to the equation.
    """
    # computing the discriminant
    d = (b**2) - (4*a*c)

    if d < 0:
        return []
    elif d == 0:
        return [(-b) / (2*a)]
    else:
        return [(-b - math.sqrt(d)) / (2*a), (-b + math.sqrt(d)) / (2*a)]