"""
QUESTION:
Write a function `generate_permutations` that takes an array of integers as input and returns all unique permutations of three numbers from the array, where each permutation must contain exactly two odd numbers and one even number. The input array may contain duplicates, but the output permutations should not have any duplicates.
"""

import itertools

def generate_permutations(numbers):
    permutations = set()
    
    # Generate all permutations of the given array
    all_permutations = itertools.permutations(numbers, 3)
    
    # Iterate over each permutation
    for perm in all_permutations:
        # Check if the permutation satisfies the condition
        if sum(1 for num in perm if num % 2 == 0) == 1 and sum(1 for num in perm if num % 2 == 1) == 2:
            permutations.add(perm)
    
    return permutations