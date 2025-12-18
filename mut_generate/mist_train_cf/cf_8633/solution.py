"""
QUESTION:
Write a function `multiply(x, y)` that calculates the product of two positive integers without using the multiplication operator (*), built-in multiplication functions, division, or modulo operators. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the value of the larger integer.
"""

def multiply(x, y):
    if x == 0 or y == 0:
        return 0

    if x < y:
        x, y = y, x

    result = 0

    while y > 0:
        if y & 1:
            result += x
        y >>= 1
        x <<= 1

    return result