"""
QUESTION:
Create a function `print_twin_primes(limit)` that prints all twin prime numbers below the given limit. A twin prime is a pair of prime numbers that differ by 2. The limit will be a positive integer, and the function should only print pairs of prime numbers that are both less than or equal to the limit.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_twin_primes(limit):
    for n in range(3, limit + 1):
        if is_prime(n) and is_prime(n + 2):
            print(f"({n}, {n + 2})")