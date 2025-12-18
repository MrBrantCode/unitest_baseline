"""
QUESTION:
Write a function `power(base, exponent)` that calculates the exponential of a given `base` raised to the power of `exponent` using only bitwise operations and loops. The function should not use any built-in functions, modules, or arithmetic operations related to exponentiation or mathematical calculations, and it should have a time complexity of O(log n), where n is the `exponent`.
"""

def entrance(base, exponent):
    if exponent == 0:
        return 1
    
    result = 1
    while exponent > 1:
        if exponent & 1:  # check if the exponent is odd
            result *= base
        
        base *= base
        exponent >>= 1  # divide the exponent by 2 using bitwise right shift
        
    return result * base