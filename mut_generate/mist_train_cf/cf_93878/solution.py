"""
QUESTION:
Write a function named `primes_sum` that takes an integer `n` as input and returns a tuple containing a list of all prime numbers smaller than or equal to `n` and their sum. The function should only consider integers in the range 2 to `n` (inclusive).
"""

def primes_sum(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    prime_sum = 0
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
            prime_sum += i
    return primes, prime_sum