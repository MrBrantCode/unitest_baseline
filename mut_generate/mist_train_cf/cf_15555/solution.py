"""
QUESTION:
Write a function named `is_anagram` that takes two strings `s1` and `s2` as input. The function should return `True` if the strings are anagrams and `False` otherwise. The comparison should be case-insensitive, ignoring differences in uppercase and lowercase letters, and should also ignore non-alphabetic characters. The function should handle strings of any length, including empty strings, and should be able to handle Unicode characters and special characters.
"""

def is_anagram(s1, s2):
    # Convert strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()

    # Remove non-alphabetic characters
    s1 = ''.join(c for c in s1 if c.isalpha())
    s2 = ''.join(c for c in s2 if c.isalpha())

    # Sort strings
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    # Compare sorted strings
    if sorted_s1 == sorted_s2:
        return True
    else:
        return False