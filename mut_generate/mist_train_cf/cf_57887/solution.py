"""
QUESTION:
Create a function named `consonants` that takes a string as input, identifies all unique consonants, and returns a dictionary with the consonants as keys and their occurrence counts as values. The function should be case-insensitive and ignore non-consonant characters.
"""

def consonants(s):
    s = s.lower()
    consonants = 'bcdfghjklmnpqrstvwxyz'
    unique_consonants = set([char for char in s if char in consonants])
    result = {char: s.count(char) for char in unique_consonants}
    return result