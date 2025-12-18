"""
QUESTION:
Implement a function named `is_anagram` that takes two strings as input, removes non-alphanumeric characters, and checks whether they are anagrams. The function should return True if the strings are anagrams and False otherwise. The comparison should be case-insensitive.
"""

def is_anagram(str1, str2):
    # Remove spaces and punctuation
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())

    # Convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort the strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Check if the sorted strings are equal
    return str1 == str2