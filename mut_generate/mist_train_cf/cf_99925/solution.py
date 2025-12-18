"""
QUESTION:
Create a function named `find_anagrams` that takes a string `s` as input and returns a set of all possible anagrams of `s`. The function should remove duplicates and consider each anagram as a distinct element regardless of order or case.
"""

from itertools import permutations

def find_anagrams(s):
    perms = permutations(s)
    anagrams = set(''.join(p) for p in perms)
    return anagrams