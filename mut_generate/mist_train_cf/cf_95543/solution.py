"""
QUESTION:
Generate all unique permutations of a given array of numbers, where each permutation must contain exactly two odd numbers and one even number. The original array may contain duplicate numbers, but the permutations should not have any duplicates. Implement a function `generate_permutations(numbers)` that returns these permutations.
"""

import itertools

def generate_permutations(numbers):
    permutations = []
    
    # Generate all permutations of the array
    all_permutations = list(itertools.permutations(numbers))
    
    for perm in all_permutations:
        odd_count = 0
        even_count = 0
        
        for num in perm:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        # Check if the permutation satisfies the condition
        if odd_count == 2 and even_count == 1:
            permutations.append(list(perm))
    
    return permutations