"""
QUESTION:
Write a function, `check_sign_difference`, that takes two integers, `x` and `y`, as input and returns `True` if the signs of `x` and `y` are different, and `False` otherwise. The function should not use logical operators (`and`, `or`, `not`) or conditional structures (`if`, `switch`, `case`).
"""

def check_sign_difference(x, y):
    return (x^y) < 0