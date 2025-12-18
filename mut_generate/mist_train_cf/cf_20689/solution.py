"""
QUESTION:
Write a function `quadratic_roots(a, b, c)` that calculates the roots of a quadratic equation `ax^2 + bx + c = 0` and returns the roots as a tuple of two floats if there are two real solutions, a single float if there is one real solution, or a string "No real solutions" if there are no real solutions.
"""

import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    # Case 1: Two real solutions
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    
    # Case 2: One real solution
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    
    # Case 3: No real solutions
    else:
        return "No real solutions"