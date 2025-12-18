"""
QUESTION:
Create a function `find_primes(n)` that determines all prime numbers in a sequence up to a predefined value `n`. The function should return a list of prime numbers. The input `n` is an integer and the output is a list of integers. The function should only consider numbers from 2 up to `n` (inclusive) and identify prime numbers by checking divisibility up to the square root of each number.
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