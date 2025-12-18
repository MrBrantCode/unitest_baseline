"""
QUESTION:
Write a function `generate_primes(n)` that generates the first `n` prime numbers. The function should take an integer `n` as input and return a list of the first `n` prime numbers. The function should not take any other inputs or prompts, and the input `n` is assumed to be a positive integer.
"""

def generate_primes(n):
    def is_prime(num):
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