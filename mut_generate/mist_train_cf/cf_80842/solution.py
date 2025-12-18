"""
QUESTION:
Develop a function `solve_quadratic_roots` to find the roots of a quadratic equation `ax^2 + bx + c = 0`, considering both real and complex roots, without using the quadratic formula. The function should take three parameters: `a`, `b`, and `c`, where `a` is non-zero.
"""

import cmath

def solve_quadratic_roots(a, b, c):
    """
    Find the roots of a quadratic equation ax^2 + bx + c = 0, 
    considering both real and complex roots, without using the quadratic formula.

    Args:
        a (float): The coefficient of the quadratic term. Non-zero.
        b (float): The coefficient of the linear term.
        c (float): The constant term.

    Returns:
        tuple: The roots of the quadratic equation.
    """

    #ax^2 + bx + c = 0 to ax^2 + bx = -c
    c = -c

    #ax^2 + bx = -c to a(x^2 + bx/a) = -c to a(x^2 + b/ax) = -c
    b = b/a

    #The perfect square trinomial will be (x + b/(2a))^2 = (x + b/2)^2
    #add (b/2)^2 to both sides.
    perfect_square_trinomial = (b/2)**2
    c += perfect_square_trinomial

    #take the square root of both sides to solve for x
    sqrt_lhs = cmath.sqrt(perfect_square_trinomial) #square root of left hand side
    sqrt_rhs = cmath.sqrt(c) #square root of right hand side

    #solve for x
    x1 = -b/2 + sqrt_rhs
    x2 = -b/2 - sqrt_rhs

    return x1, x2