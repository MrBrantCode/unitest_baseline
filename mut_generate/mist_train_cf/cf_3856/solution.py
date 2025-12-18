"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that takes in a positive integer `n` as input and returns an array of all the prime numbers up to `n`. The function should have a time complexity of O(n log log n), not O(n^2), as O(n^2) would be inefficient for this algorithm. It should use the Sieve of Eratosthenes algorithm to determine prime numbers and handle edge cases such as `n = 0` or `n = 1`, returning an empty array in such cases.
"""

def entrance(n):
    if n <= 1:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes