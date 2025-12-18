"""
QUESTION:
Write a function called `generate_primes(n)` that takes an integer `n` as input and returns a list of all prime numbers less than or equal to `n`.
"""

def generate_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes