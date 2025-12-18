"""
QUESTION:
Write a function `find_largest_prime` that takes a list of integers as input and returns the largest prime number in the list. If no prime numbers exist in the list, return `None`. Assume that the input list can be empty and may contain duplicate or negative numbers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime(lst):
    largest_prime = None
    for num in lst:
        if largest_prime is None or num > largest_prime:
            if is_prime(num):
                largest_prime = num
    return largest_prime