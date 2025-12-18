"""
QUESTION:
Create a function `sieve_of_eratosthenes` that takes a positive integer `n` as input and returns an array of all prime numbers up to `n`. The function should have a time complexity of O(n^1.5) and should not use any external libraries or built-in functions to check for prime numbers. If `n` is 0 or 1, the function should return an empty array.
"""

def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes