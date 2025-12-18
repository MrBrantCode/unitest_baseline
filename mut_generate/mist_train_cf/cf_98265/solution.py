"""
QUESTION:
Create a function named `solve_linear_equation` that takes in three parameters (a, b, and c) representing the coefficients of a linear equation in the form ax + by = c and returns the values of x and y. The function should use the formulae x = (c - by) / a and y = (c - ax) / b.
"""

def solve_linear_equation(a, b, c):
    # Initialize variable y to avoid NameError
    y = 0
    x = (c - b*y) / a
    # Update y with the calculated x value
    y = (c - a*x) / b
    return x, y