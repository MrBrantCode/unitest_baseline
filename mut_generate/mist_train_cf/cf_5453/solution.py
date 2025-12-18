"""
QUESTION:
Develop a function named `power` that takes two arguments, `base` and `exponent`, and returns the result of the power operation. Implement the power algorithm using a recursive approach with a time complexity of O(log n), where n is the exponent number. The function should handle negative exponents and return a float if necessary, without using the built-in power function or external libraries.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    elif exponent % 2 == 0:
        return power(base, exponent//2) ** 2
    else:
        return base * power(base, exponent-1)