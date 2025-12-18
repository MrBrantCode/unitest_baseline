"""
QUESTION:
Write a function called `is_prime_product(a)` that takes an integer `a` as input and returns `True` if `a` is the product of two prime numbers, and `False` otherwise. The input integer `a` is guaranteed to be less than 200.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_product(a):
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            if is_prime(i) and is_prime(a//i):
                return True
    return False