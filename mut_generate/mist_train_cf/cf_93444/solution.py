"""
QUESTION:
Create a function called `quadratic_roots` that takes three complex coefficients `a`, `b`, and `c` of a quadratic equation as input and returns the roots of the equation with a precision of up to 5 decimal places. The function should handle all possible cases: real, complex, and repeated roots.
"""

import cmath

def quadratic_roots(a, b, c):
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)
    
    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        # Calculate real roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        
        # Return the real roots
        return round(root1.real, 5), round(root2.real, 5)
    
    elif discriminant == 0:
        # Calculate a single real root
        root = -b / (2 * a)
        
        # Return the real root
        return round(root.real, 5)
    
    else:
        # Calculate complex roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        
        # Return the complex roots
        return round(root1.real, 5) + round(root1.imag, 5) * 1j, round(root2.real, 5) + round(root2.imag, 5) * 1j