"""
QUESTION:
Implement a function `multiply(x, y)` that calculates the product of two positive integers `x` and `y` without using the multiplication operator or any built-in functions or methods that involve multiplication. Both `x` and `y` are less than or equal to 1000.
"""

def multiply(x, y):
    result = 0
    for i in range(y):
        result += x
    return result