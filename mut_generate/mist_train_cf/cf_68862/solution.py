"""
QUESTION:
Implement a function `power(x, n)` that calculates the nth power of a given number x without using any built-in exponent or power functions. The function should take two parameters: the base number x and the exponent n. The function should return the result of x to the power of n.
"""

def entance(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result