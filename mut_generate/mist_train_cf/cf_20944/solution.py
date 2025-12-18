"""
QUESTION:
Create a function `is_anagram` that takes two strings `str1` and `str2` as input, removes spaces, punctuation marks, and special characters, and checks if the remaining characters are anagrams in a case-insensitive manner. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def is_anagram(str1, str2):
    # Remove spaces, punctuation marks, and special characters from the strings
    str1 = ''.join(c for c in str1 if c.isalnum())
    str2 = ''.join(c for c in str2 if c.isalnum())

    # Convert the strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Check if the sorted strings are equal (anagrams)
    return sorted(str1) == sorted(str2)