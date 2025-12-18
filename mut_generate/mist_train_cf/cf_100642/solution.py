"""
QUESTION:
Write a function named `is_anagram` that takes two string inputs and returns a boolean indicating whether they are anagrams, disregarding case and whitespace.
"""

import collections
import string

def is_anagram(str1, str2):
    str1 = str1.translate(str.maketrans("", "", string.whitespace)).lower()
    str2 = str2.translate(str.maketrans("", "", string.whitespace)).lower()
    freq1 = collections.Counter(str1)
    freq2 = collections.Counter(str2)
    return freq1 == freq2