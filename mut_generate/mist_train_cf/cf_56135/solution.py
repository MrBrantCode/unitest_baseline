"""
QUESTION:
Write a function called `generate_permutations` that takes a list of distinct uppercase English alphabetic characters as input and returns all distinct rearrangements of the characters. The function should not take any additional parameters and must return a list of strings, where each string is a rearrangement of the input characters. The function must handle inputs of any length, but may assume that the input list is not empty.
"""

from itertools import permutations

def generate_permutations(chars):
    """
    Generate all distinct rearrangements of the characters in the input list.
    
    Parameters:
    chars (list): A list of distinct uppercase English alphabetic characters.
    
    Returns:
    list: A list of strings, where each string is a rearrangement of the input characters.
    """
    # Use the permutations function to generate all permutations of the input iterable
    perm = permutations(chars)
    
    # Convert the iterator to a list of strings and return the result
    return [''.join(i) for i in perm]