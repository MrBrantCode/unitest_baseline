"""
QUESTION:
Write a function `generate_combinations(list1, list2)` that takes two lists of integers as input and returns a list of tuples. Each tuple contains one element from `list1` and one element from `list2`, where the first element is a prime and odd perfect square, the second element is a power of 2 and a multiple of 10, and the two elements are not both divisible by 3. The tuples should be sorted in ascending order based on the sum of their elements. The length of each input list should be at least 5, and the length of each tuple should be exactly 2.
"""

import itertools
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_combinations(list1, list2):
    combinations = list(itertools.product(list1, list2))
    valid_combinations = []
    for combination in combinations:
        if combination[0] % 2 == 1 and combination[1] > 6 and is_prime(combination[0]) and math.sqrt(combination[0]) == int(math.sqrt(combination[0])) and combination[1] % 10 == 0 and combination[1] & (combination[1] - 1) == 0 and combination[0] % 3 != 0 and combination[1] % 3 != 0:
            valid_combinations.append(combination)
    valid_combinations.sort(key=lambda x: sum(x))
    return valid_combinations