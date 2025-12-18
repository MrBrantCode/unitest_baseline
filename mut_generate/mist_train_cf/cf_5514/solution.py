"""
QUESTION:
Implement a function `exponent(x, y)` to calculate the exponent of a given number `x` raised to power `y` using bitwise operations. The function should achieve a time complexity of O(log y) and a space complexity of O(1), without using any built-in exponentiation functions or operators.
"""

def exponent(x, y):
    result = 1
    while y > 0:
        if y & 1:   # check if the least significant bit of y is 1
            result *= x
        x *= x      # square x for the next iteration
        y >>= 1     # right shift y by 1 to divide it by 2
    return result