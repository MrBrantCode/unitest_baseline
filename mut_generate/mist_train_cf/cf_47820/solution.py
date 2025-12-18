"""
QUESTION:
Write a function `solve_quadratic(a, b, c)` that takes the coefficients a, b, and c of a quadratic equation ax^2 + bx + c = 0 as input and returns its solutions. The function should account for the following conditions: 
- If the equation has no real solutions, return "No real solutions".
- If the equation has one real solution, return the solution.
- If the equation has two real solutions, return both solutions. 

The solutions should be saved to a text file and the function should also be able to retrieve the solutions from the file.
"""

import cmath

def solve_quadratic(a, b, c):
    # Calculate discriminant
    discriminant = (b**2) - (4*a*c)
    
    # Check for number of solutions
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        return x1, x2