"""
QUESTION:
Write a function `generate_prime_array` that takes an integer `n` as input and returns a list of all prime numbers up to and including `n`. The function should not include 0 or 1 in the output.
"""

def generate_prime_array(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes