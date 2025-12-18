"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of an integer `n`. The function should return `None` if `n` is a negative integer, and the correct factorial result for non-negative integers, with the additional requirement that the factorial of a negative integer `n` should be calculated as if the input was `|n|` but with a negative sign.
"""

def factorial(n):
    if n < 0:
        sign = -1
        n = abs(n)
    else:
        sign = 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return sign * result