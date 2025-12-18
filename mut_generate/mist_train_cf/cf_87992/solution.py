"""
QUESTION:
Create two functions: `generate_prime_numbers(n)` and `sum_prime_numbers(prime_numbers)`. `generate_prime_numbers(n)` should take an integer `n` as input and return a list of all prime numbers between 1 and `n` (inclusive). `sum_prime_numbers(prime_numbers)` should take a list of prime numbers as input and return the sum of those prime numbers. The time complexity of both functions should be optimized as much as possible.
"""

def entrance(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = []
    for i in range(2, n+1):
        if primes[i]:
            prime_numbers.append(i)

    return sum(prime_numbers)