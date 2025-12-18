"""
QUESTION:
Create a function named `quadratic_roots` that takes in the coefficients a, b, and c of a quadratic equation and returns its roots, which can be real or complex. The function should handle quadratic equations with complex coefficients and display the results with a precision of up to 5 decimal places.
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