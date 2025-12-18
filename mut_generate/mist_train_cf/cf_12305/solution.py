"""
QUESTION:
Create a function called `power` that takes two parameters: `base` and `p`. The function should raise `base` to the power of `p` using only basic arithmetic operations (addition, subtraction, multiplication, and division) without using any built-in exponentiation functions or operators.
"""

def power(base, p):
    if p == 0:
        return 1
    
    result = 1
    abs_p = abs(p)
    
    while abs_p > 0:
        if abs_p % 2 == 1:
            result *= base
        
        base *= base
        abs_p //= 2
    
    return result if p > 0 else 1/result