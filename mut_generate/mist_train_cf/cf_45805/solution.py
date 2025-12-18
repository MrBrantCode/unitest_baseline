"""
QUESTION:
Write a function `is_multiply_prime(a)` that takes an integer `a` less than 100 as input and returns `True` if `a` can be expressed as the product of exactly three prime numbers, and `False` otherwise.
"""

def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            a //= i
            if len(factors) > 3:
                return False
    return len(factors) == 3 and is_prime(a)