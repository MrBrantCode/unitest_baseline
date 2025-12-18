"""
QUESTION:
Create a function named `sieve_of_eratosthenes` that takes a positive integer `n` as input and returns an array of all prime numbers up to `n`. The function should have a time complexity of O(n^2) and not use any external libraries or built-in functions to check for prime numbers. It should handle edge cases where `n` is less than or equal to 1 by returning an empty array.
"""

def sieve_of_eratosthenes(n):
    if n <= 1:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes