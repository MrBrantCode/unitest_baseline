"""
QUESTION:
Create a function `is_prime(n)` that takes a single integer `n` as input. The function should return `True` if `n` is a prime number and `False` otherwise. The input `n` must be a positive integer greater than 1 and less than or equal to 10^9.
"""

def is_prime(num):
    if num < 2 or num > 10**9:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True