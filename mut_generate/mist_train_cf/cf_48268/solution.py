"""
QUESTION:
Create a function named `check_primality(n)` that determines whether a given integer `n` is prime or not, returning `True` if it's prime and `False` otherwise. The function should handle integers of all values.
"""

def check_primality(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True