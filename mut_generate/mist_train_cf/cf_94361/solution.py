"""
QUESTION:
Implement a function `product(num1, num2)` that calculates the product of two numbers without using the multiplication operator (*) or any built-in multiplication functions. The function should handle cases where one or both input numbers are negative and must be implemented using bitwise operations and/or bitwise shifting.
"""

def product(num1, num2):
    result = 0
    isNegative = False
    
    if num1 < 0 and num2 < 0:
        num1 = abs(num1)
        num2 = abs(num2)
    elif num1 < 0 or num2 < 0:
        isNegative = True
        if num1 < 0:
            num1 = abs(num1)
        else:
            num2 = abs(num2)
    
    while num1 > 0:
        if num1 & 1:
            result += num2
        num1 >>= 1
        num2 <<= 1
    
    if isNegative:
        result = -result
    
    return result