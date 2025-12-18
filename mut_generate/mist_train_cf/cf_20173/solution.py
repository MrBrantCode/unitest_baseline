"""
QUESTION:
Write a function `exponent(x, y)` to calculate the exponent of a given number `x` raised to power `y` without using any built-in exponentiation functions or operators. The function should have a time complexity of O(log y) and a space complexity of O(1).
"""

def exponent(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        x *= x
        y //= 2
    return result