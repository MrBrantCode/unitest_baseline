"""
QUESTION:
Write a function `is_prime(n)` that checks whether the input `n` is a prime number or not. The function should return `True` if `n` is prime and `False` otherwise. The function should accept only integers as input and should be efficient for large inputs. It should return `False` for non-positive integers and non-integer inputs.
"""

import math

def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True