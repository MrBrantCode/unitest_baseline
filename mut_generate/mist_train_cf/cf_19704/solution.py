"""
QUESTION:
Implement a function `ternary_operator` that takes an integer `x` as input and returns the result of the following expression: if `x` is greater than 0, return 10; if `x` is less than -5 and even, return -10; if `x` is divisible by 3, return 0; otherwise, return 5.
"""

def ternary_operator(x):
    return 10 if x > 0 else -10 if x < -5 and x % 2 == 0 else 0 if x % 3 == 0 else 5