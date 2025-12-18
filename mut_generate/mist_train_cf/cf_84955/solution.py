"""
QUESTION:
Write a function `is_multiply_unique_prime(num)` that takes an integer `num` as input and returns a boolean value. The function should return `True` if `num` is the product of three distinct prime numbers that have not been used before in the function call, and `False` otherwise. The function should also handle numbers less than 10,000. The function should maintain a global list of used prime numbers.
"""

used_primes = []

def is_multiply_unique_prime(num):
    global used_primes

    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(num // i):
                factors.add(num // i)

    if len(factors) != 3:
        return False
    else:
        for prime in factors:
            if prime in used_primes:
                return False
        used_primes.extend(factors)

    return True