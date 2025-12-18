"""
QUESTION:
Write a function named `get_anagram(word)` that takes a string `word` as input and returns a string representing an anagram of the input word. The anagram should be a valid word that exists in the given list of words. If no valid anagram is found, return `None`. The function should be case sensitive and consider the input word as a valid anagram if no other valid anagram is found.
"""

import itertools

def get_anagram(word):
    # Generate all possible permutations of the letters in the word
    permutations = itertools.permutations(word)
    
    # Check each permutation to see if it is a valid word
    for permutation in permutations:
        anagram = ''.join(permutation)
        if anagram in dictionary and anagram != word:
            return anagram
    
    # If no valid anagram is found, return None or the original word
    return word