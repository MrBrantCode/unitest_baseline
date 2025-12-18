"""
QUESTION:
Write a function named `prime_combinations` that prints all unique combinations of the input list of integers where each combination includes at least two elements and the sum of the elements in each combination is a prime number.
"""

from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_combinations(nums):
    combinations_list = []

    # Generate all combinations of the array
    for r in range(2, len(nums) + 1):
        combinations_list += list(combinations(nums, r))

    # Print unique combinations that sum up to a prime number
    for comb in set(combinations_list):
        if is_prime(sum(comb)):
            print(comb)