"""
QUESTION:
Compute the quantity of permutations from 1 to `n` such that prime numerals occupy prime indices (1-indexed), and return the solution modulo `10^9 + 7`. `n` is a positive integer between 1 and 100 (inclusive). The function should be named `numPrimeArrangements` and take an integer `n` as its argument.
"""

def numPrimeArrangements(n):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return (n * factorial(n - 1)) % (10**9 + 7)

    def sieve(n):
        primes = [False, False] + [True for _ in range(2, n + 1)]
        p = 2
        while (p * p <= n):
            if (primes[p] == True):
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes

    primes = sieve(n)
    num_primes = sum(primes)
    num_composites = n - num_primes
    return (factorial(num_primes) * factorial(num_composites)) % (10**9 + 7)