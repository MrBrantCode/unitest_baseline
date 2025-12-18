"""
QUESTION:
Write a function named `power` that calculates the result of raising a given `base` number to a given `exponent`. The function should have a time complexity of O(log n), where n is the exponent number, and return a float if the exponent is negative. Implement the power algorithm using a recursive approach without using the built-in power function or external libraries.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    
    if exponent < 0:
        return 1 / power(base, -exponent)
    
    if exponent % 2 == 0:
        return power(base * base, exponent // 2)
    
    return base * power(base * base, (exponent - 1) // 2)