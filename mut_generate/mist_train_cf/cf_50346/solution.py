"""
QUESTION:
Write a function named `prime_numbers(n)` that takes an integer `n` and returns a list of prime numbers from 2 to `n`. The function should iterate over all numbers in the given range and identify prime numbers by checking if they have any divisors other than 1 and themselves. The function should have a time complexity of O(n^2) due to its nested loop structure.
"""

def prime_numbers(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes