"""
QUESTION:
Write a function named `generate_combinations` that takes a list of numbers as input and returns a list of all combinations of these numbers, where the sum of each combination is a prime number and the length of each combination is equal to the number of elements in the input list. The function should not return combinations with repeated numbers.
"""

import itertools

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_combinations(nums):
    combinations = []
    for combo in itertools.combinations(nums, len(nums)):
        if is_prime(sum(combo)):
            combinations.append(combo)
    return combinations