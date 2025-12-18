"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of all prime numbers from 1 to a given number `n`. The function should take one argument `n`, which is a positive integer. The function should return the sum of all prime numbers in the range from 1 to `n`.
"""

def sum_of_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return sum(primes)