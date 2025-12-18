"""
QUESTION:
Create a function named `is_prime` that determines whether a given integer is a prime number. The function should take an integer `n` as input, where 2 ≤ `n` ≤ 10^9. It should return `True` if `n` is prime and `False` otherwise. The time complexity of the function should be O(sqrt(n)).
"""

import math

def entrance(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    
    return True