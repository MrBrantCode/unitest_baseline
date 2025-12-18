"""
QUESTION:
Create a function called `primes_up_to_n` that takes a positive integer `n` as input and returns an array of all the prime numbers up to `n`. Implement the Sieve of Eratosthenes algorithm without using any external libraries or built-in functions to check for prime numbers. The function should handle edge cases such as `n = 0` or `n = 1`, and return an empty array in such cases. The function should have a time complexity of O(n^2).
"""

def primes_up_to_n(n):
    if n <= 1:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]