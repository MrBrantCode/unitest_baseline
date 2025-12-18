"""
QUESTION:
Create a function `cubic_polynomial` that evaluates the cubic polynomial expression `3x^3 + 4x - 2` for a given input `x`. The function should take in `x` as a required argument and have default parameters for the coefficients of the polynomial.
"""

def cubic_polynomial(x, leading_coefficient=3, linear_coefficient=4, constant=-2):
    return (leading_coefficient * (x ** 3)) + (linear_coefficient * x) + constant