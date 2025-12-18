"""
QUESTION:
Write a function named `is_divisible` that takes two integer variables `x` and `y` and returns a boolean value indicating whether `x` is divisible by `y` without using arithmetic operators (+, -, *, /) or built-in arithmetic functions. The function should only use bitwise operators and logical operators and have a time complexity of O(1).
"""

def is_divisible(x, y):
    if y == 1:
        return True
    if x < y or y == 0:
        return False
    return (y & (y - 1)) == 0 and x & ~(y - 1) == x