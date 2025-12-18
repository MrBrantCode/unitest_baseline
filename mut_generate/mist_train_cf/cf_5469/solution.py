"""
QUESTION:
Write a function named `calculate_quadratic_roots` that takes three coefficients `a`, `b`, and `c` as input and calculates the roots of the quadratic equation. The function should check that the inputs are numeric values, handle cases where the discriminant is negative, and check if the calculated roots are irrational numbers. The function should return the roots of the quadratic equation if they exist, or display an error message otherwise. The coefficient `a` should not be zero.
"""

import math

def calculate_quadratic_roots(a, b, c):
    # Check if the user inputs three coefficients
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        print("Error: Coefficients must be numeric values.")
        return
    
    # Check if coefficient a is not zero
    if a == 0:
        print("Error: The coefficient a cannot be zero.")
        return
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is negative
    if discriminant < 0:
        print("Error: No real roots exist for the quadratic equation.")
        return
    
    # Calculate the roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    # Check if the roots are irrational numbers
    if not (isinstance(root1, (int, float)) and isinstance(root2, (int, float))):
        print("The roots are irrational numbers.")
    
    return root1, root2