"""
QUESTION:
Implement a function `sieve_of_eratosthenes(limit)` that takes an integer `limit` as input and returns a list of all prime numbers up to `limit`. The function should use the Sieve of Eratosthenes algorithm and have a time complexity of O(n log log n) and space complexity of O(n), where n is the input `limit`.
"""

def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes