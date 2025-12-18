"""
QUESTION:
Create a function called `is_anagram` that takes two strings `str1` and `str2` as input. The function should return `True` if the alphanumeric substrings of `str1` and `str2` are anagrams, ignoring case, spaces, punctuation marks, and special characters. The function should have a time complexity of O(nlogn), where n is the length of the input strings.
"""

import re

def is_anagram(str1, str2):
    # Remove spaces, punctuation marks, and special characters
    str1 = re.sub(r'[^a-zA-Z]', '', str1)
    str2 = re.sub(r'[^a-zA-Z]', '', str2)

    # Convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort the modified strings
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    # Compare the sorted strings
    return str1 == str2