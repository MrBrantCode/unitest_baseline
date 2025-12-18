"""
QUESTION:
Create a function called `is_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be able to handle large numbers efficiently.
"""

def is_prime(n):
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