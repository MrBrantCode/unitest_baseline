"""
QUESTION:
Implement a function `f(x)` that takes an integer `x` and returns the result of the recursive calculation: `f(x) = 0` if `x` is 1, otherwise `f(x) = x * f(x - 1) + x**2`. The function should only accept non-negative integers.
"""

def f(x):
    if x == 1:
        return 0
    else:
        return x * f(x - 1) + x**2