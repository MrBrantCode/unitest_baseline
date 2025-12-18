"""
QUESTION:
Write a function `primes_and_composites(switch)` that takes a boolean value `switch` and returns a list of prime numbers if `switch` is `True` or a list of composite numbers if `switch` is `False`. The list should contain numbers in the range of 2 to 500.
"""

def primes_and_composites(switch):
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

    primes = [n for n in range(2, 501) if is_prime(n)]
    composites = [n for n in range(2, 501) if not is_prime(n)]

    return primes if switch else composites