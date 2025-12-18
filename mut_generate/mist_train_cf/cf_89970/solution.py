"""
QUESTION:
Write a function `count_combinations(target_sum)` that calculates the number of unique combinations of four digits from 0 to 9, where the sum of the four digits is equal to `target_sum`. The function should return the count of such combinations.
"""

from itertools import combinations

def count_combinations(target_sum):
    digits = list(range(10))  
    combinations_count = 0  
    
    for combination in combinations(digits, 4):
        if sum(combination) == target_sum:
            combinations_count += 1  
    
    return combinations_count