"""
QUESTION:
Create a function named `calculate_anagrams` that takes a string as input and returns the number of anagrams and a list of all the anagrams found, with the restriction that the anagrams must not contain any repeating characters.
"""

import itertools

def calculate_anagrams(string):
    permutations = itertools.permutations(string)
    anagrams = []
    
    for permutation in permutations:
        if len(set(permutation)) == len(string):
            anagrams.append(''.join(permutation))
    
    return len(anagrams), anagrams