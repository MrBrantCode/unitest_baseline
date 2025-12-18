"""
QUESTION:
Write a function named `is_anagram` that takes two strings as input and returns a boolean value. The function should consider the strings as case-insensitive and ignore leading and trailing white spaces. It should also consider punctuation marks and special characters while determining if the strings are anagrams.
"""

import re

def is_anagram(string1, string2):
    # Convert the strings to lowercase and remove leading/trailing whitespaces
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    # Remove punctuation and special characters from the strings
    string1 = re.sub(r'[^\w\s]', '', string1)
    string2 = re.sub(r'[^\w\s]', '', string2)

    # Sort the characters in both strings
    sorted_string1 = sorted(string1.replace(" ", ""))
    sorted_string2 = sorted(string2.replace(" ", ""))

    # Check if the sorted strings are equal
    return sorted_string1 == sorted_string2