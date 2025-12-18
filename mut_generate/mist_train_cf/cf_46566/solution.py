"""
QUESTION:
Write a function to generate all possible combinations and permutations of a given array where the length of each subset is 3. The function should return two sets of results: one for permutations and one for combinations.
"""

import itertools

def generate_permutations_and_combinations(array, length):
    """
    Generates all possible permutations and combinations of a given array.
    
    Parameters:
    array (list): The input array.
    length (int): The length of each subset.
    
    Returns:
    tuple: A tuple containing a set of permutations and a set of combinations.
    """
    
    # find permutations
    permutations = set(itertools.permutations(array, length))
    
    # find combinations
    combinations = set(itertools.combinations(array, length))
    
    return permutations, combinations