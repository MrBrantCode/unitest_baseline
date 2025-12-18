"""
QUESTION:
Write a function named `is_anagram` that takes two strings as input and returns True if they are anagrams, False otherwise. The comparison should be case-insensitive, ignore non-alphabetic characters, and handle strings of any length, including empty strings, and Unicode characters.
"""

def is_anagram(s1, s2):
    # Remove non-alphabetic characters and convert to lowercase
    s1 = ''.join(filter(str.isalpha, s1.lower()))
    s2 = ''.join(filter(str.isalpha, s2.lower()))
    
    # Check if the sorted strings are equal
    return sorted(s1) == sorted(s2)