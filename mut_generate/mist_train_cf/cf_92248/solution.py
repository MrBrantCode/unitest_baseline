"""
QUESTION:
Create a function `power(base, p)` that raises a number `base` to a given power `p` using only basic arithmetic operations (addition, subtraction, multiplication, and division) and without using any built-in exponentiation functions or operators. The function should handle both positive and negative powers `p`.
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