"""
QUESTION:
Write a function `categorize_numbers` that takes a list of integers as input and returns two lists: one containing prime numbers and the other containing non-prime numbers, both in descending order. The function should use a single loop and achieve a time complexity of O(n√n) without utilizing built-in sorting functions.
"""

import math

def categorize_numbers(numbers):
    primes = []
    non_primes = []
    for num in numbers:
        if num < 2 or any(num % i == 0 for i in range(2, int(math.sqrt(num)) + 1)):
            non_primes.append(num)
        else:
            primes.append(num)
    primes.sort(reverse=True)
    non_primes.sort(reverse=True)
    return primes, non_primes