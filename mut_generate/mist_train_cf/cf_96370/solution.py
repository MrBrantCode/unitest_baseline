"""
QUESTION:
Develop a function named `is_anagram` that takes two strings `str1` and `str2` as input and returns a boolean indicating whether they are anagrams, ignoring non-alphanumeric characters and considering the comparison case-insensitive.
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