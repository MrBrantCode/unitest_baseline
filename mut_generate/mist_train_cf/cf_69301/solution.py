"""
QUESTION:
Write a function `solve_quadratic` that takes the coefficients `a`, `b`, and `c` of a quadratic equation ax^2 + bx + c = 0 as input and returns the solutions for x using the quadratic formula. The function should be able to handle cases with no real solutions, one real solution, and two real solutions.
"""

import math

def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation ax^2 + bx + c = 0 using the quadratic formula.
    
    Parameters:
    a (float): Coefficient of the quadratic term.
    b (float): Coefficient of the linear term.
    c (float): Constant term.
    
    Returns:
    list: A list containing the solutions for x. If there are no real solutions, returns "No real solutions."
    """
    # calculate the discriminant
    D = b**2 - 4*a*c

    if D < 0:
        return "No real solutions."
    elif D == 0:
        # one real solution
        return [-b / (2*a)]
    else:
        # two real solutions
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return [x1, x2]