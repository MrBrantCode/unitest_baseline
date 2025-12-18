"""
QUESTION:
Create a function named `filter_primes` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should use the Sieve of Eratosthenes algorithm to check for prime numbers and have a time complexity of O(n√m), where n is the length of the original list and m is the maximum value in the original list.
"""

import math

def filter_primes(numbers):
    if not numbers:
        return []

    max_value = max(numbers)
    primes = [True] * (max_value + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(max_value)) + 1):
        if primes[i]:
            for j in range(i*i, max_value+1, i):
                primes[j] = False

    return [num for num in numbers if primes[num]]