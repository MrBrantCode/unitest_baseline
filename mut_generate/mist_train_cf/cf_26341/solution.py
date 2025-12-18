"""
QUESTION:
Write a function `get_primes_up_to_n` that takes an integer `n` as input and returns an array of all prime numbers between 2 and `n` (inclusive). The function should return the prime numbers in ascending order.
"""

def get_primes_up_to_n(n):
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