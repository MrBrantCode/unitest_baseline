"""
QUESTION:
Implement a function `power(base, p)` that raises a number `base` to a given power `p` using only basic arithmetic operations (addition, subtraction, multiplication, and division) and without using any built-in exponentiation functions or operators. The function should handle negative values for both the base and the power, and return the result as a floating-point number.
"""

def power(base, p):
    if p == 0:
        return 1.0
    
    result = 1.0
    power = abs(p)
    
    while power > 0:
        if power % 2 == 0:
            base *= base
            power /= 2
        else:
            result *= base
            power -= 1
    
    if p < 0:
        result = 1.0 / result
    
    return result