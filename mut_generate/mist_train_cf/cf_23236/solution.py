"""
QUESTION:
Construct a function `is_anagram(str1, str2)` to check if two input strings are anagrams of each other. The function should ignore case and whitespace differences, and its time complexity should be O(n log n) where n is the length of the input strings. The function should return a boolean value indicating whether the input strings are anagrams.
"""

def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    return sorted(str1) == sorted(str2)