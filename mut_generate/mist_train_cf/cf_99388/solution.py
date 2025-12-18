"""
QUESTION:
Write a function `is_anagram(str1, str2)` that checks if two input strings are anagrams of each other. The function should ignore case and spaces, and return a boolean indicating whether the strings are anagrams.
"""

def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)