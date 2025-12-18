"""
QUESTION:
Write a function named `generate_combinations(s)` that generates all possible combinations and permutations of characters in the given string `s`. The function should return a list of all combinations and permutations in lexicographical order, considering both upper and lower case letters and numbers. The string `s` only contains alphanumeric characters.
"""

import itertools

def generate_combinations(s):
    characters = list(s)
    combinations = []
    
    for r in range(1, len(characters)+1):
        for combination in itertools.combinations(characters, r):
            for permutation in itertools.permutations(combination):
                combinations.append(''.join(permutation))
    
    combinations.sort()
    
    return combinations