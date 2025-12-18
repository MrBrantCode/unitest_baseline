"""
QUESTION:
Write a function named `is_anagram` that checks whether two input strings are anagrams. The function should handle cases where the strings contain special characters, whitespace, numbers, emojis, and are written in different languages and scripts, and also handle strings with different character encodings. The function should have a time complexity of O(nlogn) or less.
"""

import re

def is_anagram(string1, string2):
    # Remove special characters and numbers
    string1 = re.sub(r'[^A-Za-z]+', '', string1).lower()
    string2 = re.sub(r'[^A-Za-z]+', '', string2).lower()

    # Sort the strings
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    # Compare the sorted strings
    return sorted_string1 == sorted_string2