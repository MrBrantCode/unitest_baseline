"""
QUESTION:
Create a function named `primes_sum` that takes an integer `n` as input and returns a tuple containing a list of all prime numbers smaller than or equal to `n` and the sum of these prime numbers.
"""

def primes_sum(n):
    primes = []
    prime_sum = 0
    for i in range(2, n+1):
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            primes.append(i)
            prime_sum += i
    return primes, prime_sum