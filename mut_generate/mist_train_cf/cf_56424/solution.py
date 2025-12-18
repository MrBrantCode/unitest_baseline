"""
QUESTION:
Write a function `sqrt(x)` that takes a non-negative integer `x` as input, computes its square root, and returns the integer part of the result along with the remainder if `x` is not a perfect square. The remainder is calculated by subtracting the square of the integer part of the square root from `x`. The function should return the results as integers and handle non-negative integers within the range `0 <= x <= 2^31 - 1`.
"""

def sqrt(x):
    # Compute the integer part of the square root
    root = int(x ** 0.5)

    # Compute the remainder
    remainder = x - root * root

    return root, remainder