"""
QUESTION:
Create a function `is_anagram` that takes two strings as input and returns a boolean value indicating whether they are anagrams of each other. The function should be case-insensitive, ignore whitespace, and handle Unicode strings and special characters.
"""

import collections
import string

def is_anagram(str1, str2):
    str1 = str1.translate(str.maketrans("", "", string.whitespace)).lower()
    str2 = str2.translate(str.maketrans("", "", string.whitespace)).lower()
    freq1 = collections.Counter(str1)
    freq2 = collections.Counter(str2)
    return freq1 == freq2