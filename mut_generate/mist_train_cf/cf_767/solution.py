"""
QUESTION:
Create a function called `gcd` that takes two integers `x` and `y` as input and returns their greatest common divisor without using division, modulo, or multiplication operations, or any built-in mathematical functions. The function should repeatedly subtract the smaller number from the larger one until both numbers are equal, then return that equal value.
"""

def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x