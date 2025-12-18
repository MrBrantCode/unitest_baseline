"""
QUESTION:
Implement the `is_prime(n)` function to verify the primality of any integer `n`. The function should return `True` for prime integers and `False` for non-prime integers. The input `n` is an integer, and the function should be efficient enough to handle large inputs. The function should not use any external libraries other than the built-in `math` module.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n)+1): 
        if n % i == 0:
            return False
    return True