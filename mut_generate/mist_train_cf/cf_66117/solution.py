"""
QUESTION:
Create a function `find_primes(n)` that takes an integer `n` as input and returns a list of all prime numbers from 1 to `n` (inclusive). The function should be efficient and only iterate up to the square root of each number to check for primality.
"""

def find_primes(n):
    primes = []
    for possiblePrime in range(2, n+1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes