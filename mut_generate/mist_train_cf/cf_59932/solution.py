"""
QUESTION:
Create a function `prime_factorial_sum` that generates a list of prime numbers up to a given input number `n` (less than or equal to 100), calculates the factorial of each prime number, and returns a list of sums of each prime number and its factorial.
"""

import math

def prime_factorial_sum(n):
    primes = []
    for potentialPrime in range(2, n):
        isPrime = True
        for num in range(2, int(potentialPrime ** 0.5) + 1):
            if potentialPrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(potentialPrime)
    result = []
    for prime in primes:
        result.append(prime + math.factorial(prime))
    return result