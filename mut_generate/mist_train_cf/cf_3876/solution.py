"""
QUESTION:
Implement a function `power(a: int, b: int) -> float` that calculates the result of `a` raised to the power of `b`. The function should take two integers `a` and `b` as arguments where -10^9 <= a, b <= 10^9. You are not allowed to use any built-in functions or operators for exponentiation. The function should correctly handle negative exponents, zero base, and large numbers efficiently.
"""

def power(a: int, b: int) -> float:
    if b == 0:
        return 1.0
    elif a == 0:
        if b < 0:
            return float('inf')
        else:
            return 0.0
    
    result = 1.0
    exponent = abs(b)
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= a
        
        a *= a
        exponent //= 2
    
    if b < 0:
        return 1.0 / result
    else:
        return result