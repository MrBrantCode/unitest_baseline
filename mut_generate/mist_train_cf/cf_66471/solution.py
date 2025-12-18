"""
QUESTION:
Write a function named `is_perfect_square_of_two_primes` that takes an integer `b` as input, where `1 ≤ b ≤ 500`, and returns `True` if `b` is the perfect square of the product of two prime numbers, and `False` otherwise.
"""

def is_perfect_square_of_two_primes(b):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if b < 1 or b > 500:
        return False
    sqrt_b = b**0.5
    if sqrt_b != int(sqrt_b):
        return False  
    for i in range(2, int(sqrt_b)):
        if sqrt_b % i == 0:
            if is_prime(i) and is_prime(int(sqrt_b//i)):
                return True
    return False