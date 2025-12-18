"""
QUESTION:
Write a function `calculate_anagrams` that takes a string as input and returns the number of anagrams present in the string, considering all possible permutations of the string's characters. The string is case-sensitive, and the function should return the total count of all unique permutations.
"""

from itertools import permutations

def calculate_anagrams(string):
    """
    Calculate the number of anagrams present in the string.

    Args:
        string (str): The input string.

    Returns:
        int: The total count of all unique permutations.
    """
    all_permutations = [''.join(i) for i in permutations(string)]
    return len(all_permutations)