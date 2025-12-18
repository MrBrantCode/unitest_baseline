"""
QUESTION:
Write a method named `getExponent(n,p)` that returns the largest integer exponent `x` such that p^(x) evenly divides `n`. if `p<=1` the method should return `null`/`None` (throw an `ArgumentOutOfRange` exception in C#).
"""

def get_largest_exponent(n: int, p: int) -> int:
    if p <= 1:
        return None
    
    x = 0
    while n % p == 0:
        x += 1
        n //= p
    
    return x