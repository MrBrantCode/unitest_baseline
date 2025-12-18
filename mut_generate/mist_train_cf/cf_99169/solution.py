"""
QUESTION:
Write a function `valor(p, x)` that calculates the value of a polynomial `p` at point `x`. The polynomial `p` is represented as a list of coefficients, where `p[i]` is the coefficient of the `i-th` degree term. The function should support polynomials of any degree and coefficients of any size, and should be optimized for performance.
"""

def valor(p, x):
    n = len(p)
    result = p[n-1]
    for i in range(n-2, -1, -1):
        result = result * x + p[i]
    return result