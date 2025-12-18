"""
QUESTION:
Write a function `get_primes(start, end)` that generates a list of prime numbers between `start` and `end` (inclusive) and returns their binary representations as strings. The function should not include the '0b' prefix in the binary representation.
"""

def get_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    return [bin(n)[2:] for n in range(start, end + 1) if is_prime(n)]