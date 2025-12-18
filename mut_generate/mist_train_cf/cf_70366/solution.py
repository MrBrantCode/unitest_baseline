"""
QUESTION:
Write a function called `generate_combinations` that generates all possible combinations of a given set of numbers without repetition. The input is a list of unique integers and the output should be a list of lists, each representing a unique permutation. The order of the permutations in the output does not matter.
"""

import itertools

def generate_combinations(nums):
    """
    Generates all possible combinations of a given set of numbers without repetition.
    
    Args:
    nums (list): A list of unique integers.
    
    Returns:
    list: A list of lists, each representing a unique permutation.
    """
    return list(itertools.permutations(nums))