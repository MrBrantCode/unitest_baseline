"""
QUESTION:
Write a function `get_primes(n)` that returns the nth and (n+1)th prime numbers in ascending order. The function should also return a boolean indicating whether these two prime numbers are consecutive. The function should use an optimized algorithm with a time complexity better than O(n^2) to find the prime numbers.
"""

def get_primes(n):
    primes = []
    is_prime = [True] * (n * 10)  # assume nth prime is less than 10n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int((n * 10) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n * 10, i):
                is_prime[j] = False

    count = 0
    for i in range(2, n * 10):
        if is_prime[i]:
            count += 1
            if count == n:
                first_prime = i
            elif count == n + 1:
                return first_prime, i, first_prime + 1 == i