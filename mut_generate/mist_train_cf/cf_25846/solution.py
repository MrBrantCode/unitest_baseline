"""
QUESTION:
Write a function named `anagrams` that takes a string as input and returns a list of all possible anagrams of the input string. The function should use the itertools.permutations function to generate the anagrams. The order of the anagrams in the output list does not matter.
"""

import itertools

def anagrams(s):
    """Returns a list of all possible anagrams of the input string."""
    return ["".join(permutation) for permutation in itertools.permutations(s)]