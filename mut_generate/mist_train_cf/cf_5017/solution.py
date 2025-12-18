"""
QUESTION:
Create a function `check_number` that takes an integer `x` as input and returns a string indicating whether `x` is positive, negative, or zero. The function should be implemented in a single line of code using a ternary operator.
"""

def check_number(x):
    return "x is positive" if x > 0 else "x is negative" if x < 0 else "x is zero"