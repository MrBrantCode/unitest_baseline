"""
QUESTION:
Write a function `consonant_checker` that takes a string `s` as input and returns a dictionary containing the count of each consonant in the string if it only contains consonants, otherwise returns `False`. The string should not contain any special characters or numbers.
"""

def consonant_checker(s):
    # Create a set of consonants
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = {}
    
    for char in s:
        # If the character is not in the set of consonants
        if char not in consonants:
            return False
        else:
            count[char] = count.get(char, 0) + 1
    
    return count