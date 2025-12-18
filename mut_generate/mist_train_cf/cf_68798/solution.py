"""
QUESTION:
Create a function `check_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should be optimized for efficiency.
"""

def check_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True