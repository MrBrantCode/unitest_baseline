"""
QUESTION:
Create a function `last_n_primes(n)` that takes an integer `n` as input and returns an array containing the last `n` prime numbers, where `n` is a positive integer.
"""

def last_n_primes(n):
    def is_prime(num):
        # Check if a number is prime
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes