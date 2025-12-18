"""
QUESTION:
Create a function named `power` that takes two parameters, `base` and `p`, and returns the result of raising `base` to the power `p` as a floating-point number. The function should handle negative values for both `base` and `p`, and it can only use basic arithmetic operations (addition, subtraction, multiplication, and division).
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