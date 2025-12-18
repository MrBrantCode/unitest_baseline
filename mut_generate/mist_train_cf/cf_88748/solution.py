"""
QUESTION:
Write a function named `twin_prime_numbers` that takes a list of integers as input, returns a new list containing only the twin prime numbers from the original list in ascending order, and does not include any duplicates.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def twin_prime_numbers(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    primes = list(set(primes))
    primes.sort()
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i] + 2 == primes[i+1] or primes[i] - 2 == primes[i+1]:
            twin_primes.append(primes[i])
    return twin_primes