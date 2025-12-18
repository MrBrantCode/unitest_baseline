"""
QUESTION:
Create a function `f(n)` that takes an integer `n` as an argument and returns a list of length `n`. Each element at index `i` should be the factorial of `i` if `i` is even, and the sum of a geometric series with a common ratio of 2 and the first term of 1, up to `i` terms, if `i` is odd. The index `i` starts from 1. The function should have optimized time and space complexity.
"""

import math

def f(n):
    cache = {0: 1}          # Used to store previously computed factorials

    def factorial(i):        # Helper function for calculating the factorial
        if i not in cache:
            cache[i] = i * factorial(i-1)
        return cache[i]

    def geometric_series(i):  # Helper function for calculating the sum of the geometric series
        return 1 * (1 - 2**i) / (1 - 2)

    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(geometric_series(i))

    return result