"""
QUESTION:
Write a function called `is_pair` that takes two strings as input and returns `True` if they are a pair and `False` otherwise. Two strings are considered a pair if they have the same length, contain the same characters (ignoring case), and have the same frequency of each character. The function should be efficient enough to handle extremely large strings and should work correctly with strings containing special characters, whitespace, and Unicode characters.
"""

from collections import Counter

def is_pair(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = str1.lower()
    str2 = str2.lower()

    count1 = Counter(str1)
    count2 = Counter(str2)

    return count1 == count2