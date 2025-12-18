"""
QUESTION:
Create a function `are_anagrams(s1, s2)` that determines if two input phrases are anagrams, disregarding spaces, special characters, and capitalization. The function should be able to handle strings of up to 1M characters.
"""

import string

def are_anagrams(s1, s2):
    table = str.maketrans('', '', string.punctuation + ' ')
    s1 = s1.translate(table)
    s2 = s2.translate(table)
    return sorted(s1.lower()) == sorted(s2.lower())