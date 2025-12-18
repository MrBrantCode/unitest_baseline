"""
QUESTION:
Create a function named `common_characters` that takes two strings as input. The function should return the number of common characters between the two strings, excluding any whitespace, punctuation, and numbers from the comparison. The function should be able to handle strings in multiple languages and character sets.
"""

import re

def common_characters(str1, str2):
    # Remove whitespace, punctuation, and numbers from the strings
    str1 = re.sub(r'[^a-zA-Z]', '', str1)
    str2 = re.sub(r'[^a-zA-Z]', '', str2)
    # Convert the strings to sets of characters
    set1 = set(str1)
    set2 = set(str2)
    # Find the intersection of the sets
    common = set1.intersection(set2)
    # Return the number of common characters
    return len(common)