"""
QUESTION:
Write a function named `generate_primes` that takes an integer `n` as input and returns the first `n` prime numbers along with their sum. The function should use basic arithmetic operations and logical operators to generate prime numbers without relying on built-in mathematical functions, libraries, or the Sieve of Eratosthenes. The function should have a time complexity of O(n√n) and a space complexity of O(1).
"""

import math

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num >= 2:
            primes.append(num)
        num += 1
    return primes, sum(primes)