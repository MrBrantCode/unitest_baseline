"""
QUESTION:
Create a function `find_anagrams(s)` that takes a string `s` as input and returns all possible anagrams of that string. The function should return a set of unique anagrams.
"""

from itertools import permutations

def find_anagrams(s):
    # Find all possible permutations of the string
    perms = permutations(s)
    
    # Convert each permutation to a string and add it to a set to remove duplicates
    anagrams = set(''.join(p) for p in perms)
    
    return anagrams