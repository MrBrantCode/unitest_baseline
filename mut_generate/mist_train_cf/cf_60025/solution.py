"""
QUESTION:
Create a function called `get_anagrams` that takes an input string and returns all possible permutations of the characters in the string, treating the input as a sequence of characters without considering the validity of the resulting words.
"""

from itertools import permutations

def get_anagrams(input_string):
    return [''.join(p) for p in permutations(input_string)]