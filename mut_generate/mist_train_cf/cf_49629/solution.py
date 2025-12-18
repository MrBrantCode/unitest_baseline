"""
QUESTION:
Create a function `is_multiply_prime(a)` that takes an integer input `a` (greater than 0 and less than or equal to 100) and returns `True` if `a` is a product of exactly three distinct prime numbers, and `False` otherwise. The function should correct the existing deficiency in the loop `for 1 in range(2, a): if a % i == 0:` and incorporate an additional condition to enforce the uniqueness of the prime factors.
"""

def is_multiply_prime(a):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_factors = set()
    for i in range(2, a + 1):
        while a % i == 0 and is_prime(i):
            prime_factors.add(i)
            a //= i
    return len(prime_factors) == 3