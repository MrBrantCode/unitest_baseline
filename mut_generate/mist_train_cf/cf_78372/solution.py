"""
QUESTION:
Create a function called `is_anagram` that takes two strings as input, `str1` and `str2`, and returns a boolean value indicating whether `str1` and `str2` are anagrams of each other. The function should ignore the original order of characters in the strings and consider only the characters themselves, regardless of their frequency and case. The input strings may contain any ASCII characters.
"""

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())