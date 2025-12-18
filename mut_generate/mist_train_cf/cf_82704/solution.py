"""
QUESTION:
Write a function `is_multiply_prime(a)` that takes an integer `a` less than 100 as input and returns `True` if `a` is the product of exactly three prime numbers, and `False` otherwise.
"""

def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, a):
        if a % i == 0:
            factors.append(i)
            if is_prime(i) and len(factors) <= 3:
                a /= i
                i -= 1
            else:
                break

    return len(factors) == 3 and all(is_prime(f) for f in factors)