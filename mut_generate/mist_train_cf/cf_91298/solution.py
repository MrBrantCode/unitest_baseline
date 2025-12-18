"""
QUESTION:
Create a function called `are_anagrams` that takes two parameters, `word1` and `word2`. The function should determine if `word1` and `word2` are anagrams of each other, ignoring case and non-alphabetic characters are considered.
"""

import re

def are_anagrams(word1, word2):
    word1 = ''.join(re.findall(r'[a-z]', word1.lower()))
    word2 = ''.join(re.findall(r'[a-z]', word2.lower()))
    
    return sorted(word1) == sorted(word2)