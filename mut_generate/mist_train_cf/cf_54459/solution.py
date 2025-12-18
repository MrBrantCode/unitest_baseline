"""
QUESTION:
Create a function `check_prime(n)` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def check_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True