"""
QUESTION:
Generate the function `generate_permutations(numbers)` that takes an array of numbers as input and returns all possible permutations of the array. Each permutation must contain exactly two odd numbers and one even number. The original array may contain duplicate numbers, but the permutations should not have any duplicates.
"""

import itertools

def generate_permutations(numbers):
    permutations = []
    
    all_permutations = list(itertools.permutations(numbers))
    
    for perm in all_permutations:
        odd_count = 0
        even_count = 0
        
        for num in perm:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        if odd_count == 2 and even_count == 1:
            permutations.append(list(perm))
    
    return permutations