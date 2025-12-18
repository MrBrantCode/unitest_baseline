"""
QUESTION:
Write a function `quadratic_roots(a, b, c)` that computes the roots of the quadratic equation `ax^2 + bx + c = 0`, where `a`, `b`, and `c` are real numbers. The function should handle cases where the equation has two real solutions, one real solution, or no real solutions, and return the corresponding roots or an error message. The function should take three parameters: `a`, `b`, and `c`, and return either a tuple of two roots, a single root, or a string indicating no real solutions.
"""

import math

def entance(a, b, c):
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