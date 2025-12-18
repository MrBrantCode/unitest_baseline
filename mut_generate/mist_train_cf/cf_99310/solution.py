"""
QUESTION:
Create a function called `find_anagrams` that takes a string `s` as input and returns a collection of all possible anagrams of the string, with no duplicates.
"""

from itertools import permutations

def find_anagrams(s):
    # Find all possible permutations of the string
    perms = permutations(s)
    
    # Convert each permutation to a string and add it to a set to remove duplicates
    anagrams = set(''.join(p) for p in perms)
    
    return anagrams