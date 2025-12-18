"""
QUESTION:
Create a function named `is_anagram` that takes two phrases as input and returns `True` if they are anagrams of each other, and `False` otherwise. The function should ignore spaces and non-alphanumeric characters, and consider the phrases case-insensitively. The phrases are considered distinct.
"""

def is_anagram(str1, str2):
    # Remove all whitespace and convert strings to lower case
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Remove all non-alphabetic characters
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())

    # Check if sorted strings are equal
    return sorted(str1) == sorted(str2)