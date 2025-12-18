"""
QUESTION:
Write a function named `are_anagrams(word1, word2)` that takes two string inputs and returns a boolean value indicating whether the two input strings are anagrams of each other. The function should ignore case differences and non-alphanumeric characters.
"""

import re

def are_anagrams(word1, word2):
    word1 = re.sub(r'\W+', '', word1.lower())
    word2 = re.sub(r'\W+', '', word2.lower())
    return sorted(word1) == sorted(word2)