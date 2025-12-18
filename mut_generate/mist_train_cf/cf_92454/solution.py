"""
QUESTION:
Create a function called `find_primes` that takes an integer `n` as input, where `n` can be up to 10^9, and returns a list of all prime numbers between 0 and `n` with a time complexity of O(n log log n).
"""

def find_primes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = []
    for i in range(2, n+1):
        if primes[i]:
            prime_numbers.append(i)

    return prime_numbers