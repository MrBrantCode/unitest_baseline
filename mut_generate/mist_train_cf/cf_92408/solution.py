"""
QUESTION:
Develop a function named `power` that takes two arguments, `base` and `exponent`, and returns the result of `base` raised to the power of `exponent`. The function should have a time complexity of O(log n), where n is the `exponent`. It should handle negative exponents and return a float if necessary.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    
    if exponent < 0:
        return 1 / power(base, -exponent)
    
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    
    return result