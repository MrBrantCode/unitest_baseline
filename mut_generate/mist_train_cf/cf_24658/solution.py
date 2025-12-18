"""
QUESTION:
Implement a function `solve_equation(x)` that takes an integer `x` and returns the corresponding `y` value for the equation `4x + 2y = 32`.
"""

def solve_equation(x):
    A = 4
    B = 2
    C = 32
    
    return (C - A*x)/B