"""
QUESTION:
Create a function `find_anagrams(s)` that takes a string `s` as input and returns a set of all possible unique anagrams of `s`. The function should handle duplicate anagrams by only returning each unique anagram once.
"""

from itertools import permutations

def find_anagrams(s):
    # Find all possible permutations of the string
    perms = permutations(s)
    
    # Convert each permutation to a string and add it to a set to remove duplicates
    anagrams = set(''.join(p) for p in perms)
    
    return anagrams