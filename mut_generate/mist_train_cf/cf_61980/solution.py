"""
QUESTION:
Create a function `LCM(a: int, b: int, c: int)` that calculates the Least Common Multiple (LCM) of three integers `a`, `b`, and `c`. 

Constraints: 1 <= a, b, c <= 10^9

The function should be efficient and minimize computation time. 

The expected outputs for the test cases are: 
- LCM(3, 5, 8) = 120
- LCM(21, 14, 31) = 9578
- LCM(7, 11, 25) = 1925
- LCM(12, 15, 18) = 180
- LCM(9, 3, 1) = 9
"""

import math

def LCM(a: int, b: int, c: int) -> int:
    """
    Compute LCM of a, b, and c.

    Constraints: 1 <= a, b, c <= 10^9

    """
    # Compute LCM of a, b, and c as LCM(a, LCM(b, c))
    return a * b * c // math.gcd(a, math.gcd(b, c))