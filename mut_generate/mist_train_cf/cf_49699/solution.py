"""
QUESTION:
Implement a function `is_prime(n)` that checks if a given integer `n` is a prime number, returning `True` if it is prime and `False` otherwise, with the condition that the function must handle large numbers efficiently by only checking divisibility up to the square root of `n`.
"""

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True