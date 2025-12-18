"""
QUESTION:
Write a function named `quadratic_equation` that takes three real number parameters `a`, `b`, and `c` representing the coefficients of a quadratic equation `ax^2 + bx + c = 0`. The function should return the roots of the equation, handling cases where the equation has two real solutions, one real solution, or no real solutions, and provide a message indicating whether the equation is a perfect square trinomial.
"""

import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The quadratic equation has two real solutions: {root1}, {root2}"

    elif discriminant == 0:
        # Perfect square trinomial
        root = -b / (2*a)
        return f"The quadratic equation is a perfect square trinomial with a real solution: {root}"

    else:
        # No real solutions
        return "The quadratic equation has no real solutions."