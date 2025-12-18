"""
QUESTION:
Create two functions, `solve_quadratic` and `evaluate_quadratic`, to handle quadratic equations. The `solve_quadratic` function should take coefficients a, b, and c of a quadratic equation ax² + bx + c = 0 as input and return its roots. This function must be able to handle complex roots. The `evaluate_quadratic` function should take coefficients a, b, c and a range of x values as input and return the corresponding y values. The function must be able to scale for any given range of x values.
"""

import numpy as np
import cmath 

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    disc = b**2 - 4*a*c

    root1 = (-b - cmath.sqrt(disc)) / (2*a)
    root2 = (-b + cmath.sqrt(disc)) / (2*a)

    return root1, root2

def evaluate_quadratic(a, b, c, x_range):
    # Create the polynomial
    p = np.poly1d([a, b, c])
    
    # Compute the values
    values = np.polyval(p, x_range)

    return values