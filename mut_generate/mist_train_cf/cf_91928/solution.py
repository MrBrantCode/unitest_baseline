"""
QUESTION:
Write a function `equation_result(n, x)` that calculates the sum of squares of the terms in the sequence `(x-1)^2, (2x-3)^2, ..., (nx-(2n-1))^2` where `n` is a positive integer and `x` is any real number. The function should return the total result of the equation.
"""

def equation_result(n, x):
    result = 0
    for i in range(1, n+1):
        term = (i * x - (2*i - 1))**2
        result += term
    return result