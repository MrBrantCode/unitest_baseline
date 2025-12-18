"""
QUESTION:
Implement a function `calculate_polynomial(a, b, c, d, e, x)` that calculates the result of a polynomial equation of degree 4, f(x) = ax⁴ + bx³ + cx² + dx + e, given coefficients a, b, c, d, e, and a value x. The function should handle large coefficients without integer overflow errors. The coefficients and x can be any integer.
"""

def calculate_polynomial(a, b, c, d, e, x):
    result = a * x**4 + b * x**3 + c * x**2 + d * x + e
    return result