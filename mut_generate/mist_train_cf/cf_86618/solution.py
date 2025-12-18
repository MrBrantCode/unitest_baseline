"""
QUESTION:
Create a function called `categorize_numbers` that categorizes a given list of integers into two lists: prime numbers and non-prime numbers. The function should return these two lists, with the numbers in descending order. The function must use a single loop and have a time complexity of O(n√n).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def categorize_numbers(numbers):
    primes = []
    non_primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes.append(num)
    primes.sort(reverse=True)
    non_primes.sort(reverse=True)
    return primes, non_primes