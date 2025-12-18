"""
QUESTION:
Develop a function called `power` that takes two arguments: a base number and an exponent number. The function should calculate the result of the power operation, handle negative exponents, and return a float if necessary. The function must implement its own power algorithm using a recursive approach and have a time complexity of O(log n), where n is the exponent number.
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