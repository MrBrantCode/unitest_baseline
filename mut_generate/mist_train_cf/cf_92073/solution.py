"""
QUESTION:
Generate a function named `permutations_with_odd_even_constraint` that takes a list of integers as input and returns all unique permutations of the list where each permutation contains exactly two odd numbers and one even number. The input list may contain duplicates, but the output permutations should not have any duplicates. The function should return these permutations as tuples.
"""

import itertools

def permutations_with_odd_even_constraint(numbers):
    permutations = set()
    all_permutations = itertools.permutations(numbers)

    for perm in all_permutations:
        if sum(1 for num in perm if num % 2 == 0) == 1 and sum(1 for num in perm if num % 2 == 1) == 2:
            permutations.add(perm)

    return permutations