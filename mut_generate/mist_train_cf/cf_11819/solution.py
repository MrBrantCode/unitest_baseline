"""
QUESTION:
Create a function named `solve_quadratic_equation` that takes three parameters, `a`, `b`, and `c`, representing coefficients of a quadratic equation in the form `ax^2 + bx + c = 0`. The function should return the roots of the equation using the quadratic formula. If the discriminant (`b^2 - 4ac`) is positive, return two distinct roots; if it is zero, return one root; and if it is negative, return a message indicating that no real roots exist.
"""

import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots exist."