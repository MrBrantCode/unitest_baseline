"""
QUESTION:
Construct a function `equation_result(n, x)` that calculates the sum of squares of terms in the equation `(x-1)^2 + (2x-3)^2 + (3x-5)^2 + ... + (nx-(2n-1))^2`, where `n` is a positive integer and `x` is a real number. The function should take two arguments, `n` and `x`, and return the result of the equation.
"""

def equation_result(n, x):
    result = 0
    for i in range(1, n+1):
        term = (i * x - (2*i - 1))**2
        result += term
    return result