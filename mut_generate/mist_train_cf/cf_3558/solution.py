"""
QUESTION:
Write a function `generate_prime_numbers` that generates a list of prime numbers between a given start and end value (inclusive). The start and end values can be negative, but all prime numbers are greater than 1. The resulting list should be sorted in ascending order, not contain any duplicate values, and have a time complexity of O(n log n), where n is the number of prime numbers in the range.
"""

def generate_prime_numbers(start, end):
    isPrime = [True] * (end + 1)
    p = 2
    while p * p <= end:
        if isPrime[p]:
            for i in range(p * p, end + 1, p):
                isPrime[i] = False
        p += 1
    primes = []
    for i in range(start, end + 1):
        if i >= 2 and isPrime[i]:
            primes.append(i)
    return primes