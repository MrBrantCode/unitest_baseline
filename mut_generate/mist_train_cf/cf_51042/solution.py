"""
QUESTION:
Write a function `calculate_y` that takes an integer `x` as input and returns the value of `y`. If `x` is greater than 50, `y` should be `x + 19`. If `x` is less than or equal to 50, `y` should be `x - 20` unless `x - 20` is negative, in which case `y` should be 0. The function should have a time complexity of O(1).
"""

def calculate_y(x):
    if x > 50:
        y = x + 19
    else:
        y = max(0, x - 20)
    return y