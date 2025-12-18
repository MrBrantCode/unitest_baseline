"""
QUESTION:
Write a function `generate_primes(n)` to generate all prime numbers from 2 to `n` in ascending order. The function should return a list of prime numbers. A prime number is a natural number greater than 1 that has exactly two distinct, positive divisors: 1 and itself.
"""

def generate_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)

    return primes