"""
QUESTION:
Create a function `find_prime_numbers` that takes any number of lists of integers as arguments. For each list, it finds all prime numbers, calculates their product and sum, and returns these values in a list of tuples, where each tuple contains the list of prime numbers, their product, and their sum. If a list contains non-integer values, they are ignored. If a list is empty or contains no prime numbers, the corresponding tuple contains an empty list, and `None` for product and sum.
"""

from math import sqrt
from functools import reduce
from operator import mul

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(*args):
    result = []

    for input_list in args:
        primes = []

        if not input_list:
            result.append(([], None, None))
            continue

        try:
            nums = set(int(x) for x in input_list)
        except (TypeError, ValueError):
            nums = set(x for x in input_list if isinstance(x, int))

        for num in nums:
            if is_prime(num):
                primes.append(num)

        primes.sort()
        if primes:
            product = reduce(mul, primes)
            summation = sum(primes)
        else:
            product = None
            summation = None

        result.append((primes, product, summation))

    return result