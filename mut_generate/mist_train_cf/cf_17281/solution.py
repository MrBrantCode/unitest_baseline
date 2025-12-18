"""
QUESTION:
Create a function named `prime_numbers` that takes two parameters: `lower_limit` and `upper_limit`. The function should return a list of all prime numbers between `lower_limit` and `upper_limit` (inclusive). The function should have a time complexity of O(n * sqrt(m)), where n is the number of elements in the range and m is the average value of the range, and a space complexity of O(n), where n is the number of prime numbers in the range.
"""

import math

def prime_numbers(lower_limit, upper_limit):
    primes = []
    for num in range(lower_limit, upper_limit + 1):
        if num <= 1:
            continue
        if num <= 3:
            primes.append(num)
            continue
        if num % 2 == 0 or num % 3 == 0:
            continue
        for i in range(5, int(math.sqrt(num)) + 1, 6):
            if num % i == 0 or num % (i + 2) == 0:
                break
        else:
            primes.append(num)
    return primes