"""
QUESTION:
Write a function `count_combinations` that calculates the total count of distinct combinations of all lengths that can be formed from a given set, without any repetitive entries. The function should take a set of unique integers as input and return the total count of combinations.
"""

import itertools

def count_combinations(unique_set):
    """
    This function calculates the total count of distinct combinations of all lengths 
    that can be formed from a given set, without any repetitive entries.

    Parameters:
    unique_set (set): A set of unique integers.

    Returns:
    int: The total count of combinations.
    """
    total_count = 0
    for r in range(1, len(unique_set)+1):
        combinations = list(itertools.combinations(unique_set, r))
        total_count += len(combinations)
    return total_count