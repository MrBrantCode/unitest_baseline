"""
QUESTION:
Write a function `ternary_sign` that takes an integer `x` as input and returns a string indicating the sign of the number. The function should return "positive" for positive numbers, "negative" for negative numbers, and "zero" for zero. Implement the solution using a ternary operator.
"""

def ternary_sign(x):
    return "positive" if x > 0 else "negative" if x < 0 else "zero"