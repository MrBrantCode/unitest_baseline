"""
QUESTION:
Create a function called `quadratic_roots(a, b, c)` that takes the coefficients `a`, `b`, and `c` of a quadratic equation as input and returns a list containing the roots of the equation. The function should handle both real and complex roots, and return an empty list if the discriminant is negative.
"""

import cmath

def entance(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        sqrt_discriminant = cmath.sqrt(discriminant)
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return [root1, root2]
    elif discriminant == 0:
        root = -b / (2*a)
        return [root, root]
    else:
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(-discriminant) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return [root1, root2]