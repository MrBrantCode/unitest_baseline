"""
QUESTION:
Write a function named `prime_combinations` that generates all possible combinations of a given set of numbers, where each combination has a length equal to the number of elements in the input set and its sum is a prime number. Each combination must not contain any repeated numbers.
"""

import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_combinations(nums):
    return [combo for combo in itertools.permutations(nums) if is_prime(sum(combo))]