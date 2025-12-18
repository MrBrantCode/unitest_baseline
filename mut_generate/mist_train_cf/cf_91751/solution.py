"""
QUESTION:
Write a function `square(x)` that takes an integer `x` as input and returns its square if `x` is positive, otherwise returns 0. The function must not use the ternary expression or any built-in mathematical functions or operators.
"""

def entrance(x):
    if x > 0:
        result = 0
        for _ in range(abs(x)):
            result += x
        return result
    else:
        return 0