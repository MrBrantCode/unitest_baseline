"""
QUESTION:
Write a function named `multiply` that takes two positive integers `x` and `y` as input, both less than or equal to 1000, and returns their product without using the multiplication operator (*) or any built-in functions or methods that involve multiplication.
"""

def multiply(x, y):
    result = 0
    for i in range(y):
        result += x
    return result