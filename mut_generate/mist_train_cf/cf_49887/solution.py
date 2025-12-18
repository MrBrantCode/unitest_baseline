"""
QUESTION:
Write a function `anagram_check(list1, list2)` that compares two lists of strings and returns a list of boolean values indicating whether each corresponding pair of strings are anagrams or not. The function should ignore spaces, punctuation, and capitalization. The input lists `list1` and `list2` should have the same length.
"""

import re

def anagram_check(list1, list2):
    list1 = [re.sub('\W+', '', word).lower() for word in list1]
    list2 = [re.sub('\W+', '', word).lower() for word in list2]
    return [sorted(word1) == sorted(word2) for word1, word2 in zip(list1, list2)]