"""
QUESTION:
Write a function `quadratic_equation(a, b, c)` that calculates the roots of a quadratic equation ax^2 + bx + c = 0. The function should handle cases where the equation has two real solutions, one real solution, or no real solutions. If the equation has two real solutions, return the values of the roots. If the equation has one real solution, return a message indicating that the equation is a perfect square trinomial. If the equation has no real solutions, return a corresponding error message. The function should take three arguments: `a`, `b`, and `c`, which are the coefficients of the quadratic equation.
"""

import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)

    elif discriminant == 0:
        return "The quadratic equation is a perfect square trinomial."

    else:
        return "The quadratic equation has no real solutions."