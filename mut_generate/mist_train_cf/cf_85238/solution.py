"""
QUESTION:
Create a function named `evaluate_polynomial(x)` that calculates the value of the cubic polynomial 3x^3 + 4x - 2 for a given value of x. The function should take one argument, x, and return the computed value of the polynomial.
"""

def evaluate_polynomial(x):
    cubic = 3 * x * x * x
    linear = 4 * x
    constant = -2
    aggregate = cubic + linear + constant
    return aggregate