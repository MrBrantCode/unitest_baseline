"""
QUESTION:
Write a function named `get_greatest_common_factor` that takes two integers `x` and `y` as input and returns their greatest common factor. The function should be as efficient as possible, especially for large numbers.
"""

def get_greatest_common_factor(x, y):
    while(y):
        x, y = y, x % y
    return x