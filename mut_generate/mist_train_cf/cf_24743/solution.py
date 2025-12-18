"""
QUESTION:
Write a function called `count_primes_less_than_n` that takes an integer `n` as input and returns the number of distinct prime numbers less than `n`.
"""

def count_primes_less_than_n(n):
    """Return the number of distinct prime numbers less than n."""
    primes = []
    for possiblePrime in range(2, n):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return len(primes)