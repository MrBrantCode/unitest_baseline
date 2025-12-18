"""
QUESTION:
Write a function named `multiply` that takes two positive integers `x` and `y` as input and returns their product without using the multiplication operator (*) or any built-in multiplication functions. The function should have a time complexity of O(log n), where n is the value of the larger integer, and a space complexity of O(1).
"""

def multiply(x, y):
    # Base case
    if y == 0:
        return 0

    # Recursive case
    result = multiply(x, y >> 1) << 1
    if y & 1:
        result += x

    return result