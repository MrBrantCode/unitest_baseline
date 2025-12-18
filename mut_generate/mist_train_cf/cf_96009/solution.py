"""
QUESTION:
Create a function `exponent(x, y)` to calculate the value of x raised to the power y. The function should have a time complexity of O(log y) and a space complexity of O(1), and it cannot use any built-in exponentiation functions or operators.
"""

def exponent(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x
        x *= x
        y //= 2
    return result