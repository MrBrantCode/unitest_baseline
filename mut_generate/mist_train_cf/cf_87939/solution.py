"""
QUESTION:
Create a function `count_consonants(string)` that takes a string as input. The function should remove all non-alphabetical characters from the string, convert all uppercase letters to lowercase, and count the number of consonants remaining. The function should return the total count of consonants. The function should only consider the 26 English letters (both uppercase and lowercase) as valid characters, and any other characters should be ignored.
"""

import re

def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_count = 0

    # Remove non-alphabetical characters
    string = re.sub(r'[^a-zA-Z]', '', string)

    # Convert to lowercase
    string = string.lower()

    # Count consonants
    for char in string:
        if char in consonants:
            consonant_count += 1

    return consonant_count