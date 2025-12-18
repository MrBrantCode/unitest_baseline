"""
QUESTION:
Create a function named `sum_of_sqrt_of_primes` that takes an array of numbers as input and returns the sum of square roots of unique positive prime numbers. Return 0.0 if there are no non-negative prime numbers and None if the array is empty. Ignore non-integer, negative, and composite numbers. The sum should be rounded to two decimal places.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def sum_of_sqrt_of_primes(arr):
    if not arr:
        return None
    total = 0
    primes = []
    for num in arr:
        if num >= 0 and is_prime(num) and num not in primes:
            total += math.sqrt(num)
            primes.append(num)
    return round(total, 2)