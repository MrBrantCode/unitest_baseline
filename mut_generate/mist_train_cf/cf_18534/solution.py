"""
QUESTION:
Write a function `calculate_anagrams` that calculates the number of anagrams present in a given string without any repeating characters and returns a list of all the anagrams found. The input string will contain only lowercase English letters. The function should return the total count of anagrams and a list of all anagrams.
"""

import itertools

def calculate_anagrams(string):
    permutations = itertools.permutations(string)
    anagrams = []
    
    for permutation in permutations:
        if len(set(permutation)) == len(string):
            anagrams.append(''.join(permutation))
    
    return len(anagrams), anagrams