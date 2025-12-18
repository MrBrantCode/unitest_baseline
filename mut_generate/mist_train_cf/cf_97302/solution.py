"""
QUESTION:
Write a function `find_primes(n)` that returns the squares of the first `n` prime numbers. Do not use any pre-existing libraries or functions for finding prime numbers.
"""

def find_primes(n):
    def is_prime(num):
        if num <= 1:
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
    return [prime ** 2 for prime in primes]