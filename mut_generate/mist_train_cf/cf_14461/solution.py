"""
QUESTION:
Write a function `generate_combinations(alphabet, length)` that generates all unique string combinations of the given alphabet of a specified length, where each combination must contain at least one lowercase letter, one uppercase letter, and one digit.
"""

import itertools

def generate_combinations(alphabet, length):
    combinations = []
    
    # Generate all possible combinations of length 'length'
    for combination in itertools.combinations_with_replacement(alphabet, length):
        # Check if the combination contains at least one lowercase letter, one uppercase letter, and one digit
        if any(char.islower() for char in combination) and any(char.isupper() for char in combination) and any(char.isdigit() for char in combination):
            combinations.append(''.join(combination))
    
    return combinations