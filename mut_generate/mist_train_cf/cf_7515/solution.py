"""
QUESTION:
Write a function `count_combinations(target_sum)` that calculates the number of unique combinations of four digits from 0 to 9, where the sum of the four digits is equal to `target_sum`. The function should take an integer `target_sum` as a parameter and return the count of combinations as an integer.
"""

from itertools import combinations

def count_combinations(target_sum):
    digits = list(range(10))  # Create a list of digits from 0 to 9
    combinations_count = 0  # Initialize the count of combinations
    
    # Iterate through all possible combinations of 4 digits
    for combination in combinations(digits, 4):
        # Check if the sum of the combination is equal to the target sum
        if sum(combination) == target_sum:
            combinations_count += 1  # Increment the count of combinations
    
    return combinations_count