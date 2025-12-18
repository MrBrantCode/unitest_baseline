"""
QUESTION:
Write a function named get_anagrams that takes a string as input and returns a list of all its possible anagrams. The function should return an empty list if the input is not a string or if the string is empty.
"""

from itertools import permutations 

def get_anagrams(string):
    if not isinstance(string, str) or string == "":
        return []
    else:
        return [''.join(p) for p in permutations(string)]