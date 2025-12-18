"""
QUESTION:
Implement a function `sum_unique_primes(lst)` that takes a list of integers as input and returns the sum of all unique prime numbers in the list. The function should have a time complexity of O(n^2) and a space complexity of O(1), and should not use any built-in functions or libraries for prime number calculation.
"""

import math

def sum_unique_primes(lst):
    primes = set()
    total_sum = 0
    for num in lst:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num not in primes:
            primes.add(num)
            total_sum += num
    return total_sum