"""
QUESTION:
Create a function named 'power' that takes two arguments, 'x' and 'n', where 'x' is the base number and 'n' is the exponent. The function should return the result of 'x' raised to the power of 'n'. 'x' can be a decimal number and 'n' can be a negative number. The function must handle these cases and have a time complexity of O(log N) or better.
"""

def power(x, n):
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2

    return result