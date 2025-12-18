"""
QUESTION:
Write a function named `is_anagram` that takes two strings as input and returns True if one string is an anagram of the other, False otherwise. The function should ignore any whitespace characters in the input strings and consider them as part of the anagram. It should also handle cases where the input strings contain special characters or numbers by ignoring them. The comparison should be case-insensitive.
"""

def is_anagram(s1, s2):
    # Removing whitespace characters and converting to lowercase
    s1 = ''.join(s1.split()).lower()
    s2 = ''.join(s2.split()).lower()
    
    # Removing special characters and numbers
    s1 = ''.join(c for c in s1 if c.isalpha())
    s2 = ''.join(c for c in s2 if c.isalpha())
    
    # Checking if the sorted strings are equal
    return sorted(s1) == sorted(s2)