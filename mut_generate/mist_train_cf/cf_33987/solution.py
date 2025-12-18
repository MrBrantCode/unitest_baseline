"""
QUESTION:
Implement the `sieve_of_eratosthenes` function to generate all prime numbers up to a given limit `n` using the Sieve of Eratosthenes algorithm. The function should return a list of prime numbers.
"""

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime

    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    for p in range(int(n ** 0.5) + 1, n + 1):
        if sieve[p]:
            primes.append(p)

    return primes