"""
QUESTION:
Create a function named `count_lower(s)` that takes a string `s` as input and returns the count of lowercase consonants located at odd index positions (0-based indexing) in the string. The function should consider only the lowercase consonants 'bcdfghjklmnpqrstvwxyz' and ignore all other characters, including uppercase letters and non-alphabet characters.
"""

def count_lower(s):
    lowerConsonants = 'bcdfghjklmnpqrstvwxyz'
    count = 0
    for idx, char in enumerate(s):
        if idx % 2 != 0 and char in lowerConsonants:
            count += 1
    return count