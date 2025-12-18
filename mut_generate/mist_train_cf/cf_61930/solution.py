"""
QUESTION:
Construct a function named `filtered_primes` that takes an arbitrary non-negative integer `n` and returns a list of the first `n` prime numbers, excluding any primes divisible by 3 (excluding 3 itself).
"""

def filtered_primes(n):
    def sieve(limit):
        is_prime = [True] * (limit + 1)
        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return [i for i in range(2, limit) if is_prime[i]]

    primes = sieve(n * 10)
    filtered_primes = [prime for prime in primes if prime != 3 and prime % 3 != 0]
    return filtered_primes[:n]