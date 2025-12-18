"""
QUESTION:
Write a function `power(base, exponent)` that calculates the value of `base` raised to the power of `exponent` using only bitwise operations, loops, and recursion, without using built-in functions or modules related to exponentiation or mathematical calculations. The function should have a time complexity of O(log n), where n is the exponent.
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