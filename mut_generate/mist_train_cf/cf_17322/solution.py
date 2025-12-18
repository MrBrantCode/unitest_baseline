"""
QUESTION:
Write a function `multiply(x, n)` that takes two positive integers `x` and `n` and returns the result of multiplying `x` by itself `n` times using recursion. The function should use at least three recursion calls.
"""

def multiply(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return multiply(x, n/2) * multiply(x, n/2)
    else:
        return multiply(x, (n-1)/2) * multiply(x, (n-1)/2) * x