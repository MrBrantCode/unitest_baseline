"""
QUESTION:
Write a function `are_anagrams` that takes two strings as input, ignores case, spaces, and punctuation, and returns `True` if the strings are anagrams of each other and `False` otherwise. The function should be able to handle strings containing Unicode characters.
"""

import re
def are_anagrams(string1, string2):
    # Remove punctuation, spaces and convert to lower case
    string1 = re.sub('\W+','', string1.lower())
    string2 = re.sub('\W+','', string2.lower())

    # Return True if sorted versions of the strings are equal
    return sorted(string1) == sorted(string2)