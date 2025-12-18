"""
QUESTION:
Create a function called `get_primes` that returns an array of integers containing all prime numbers within a specified range (inclusive). The function should take one argument `n` representing the upper limit of the range, and it should return all prime numbers between 1 and `n`.
"""

def get_primes(n):
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