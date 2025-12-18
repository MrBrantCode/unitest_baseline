"""
QUESTION:
Write a function called `is_anagram(s1, s2)` that takes two strings as input and returns True if they are anagrams, False otherwise. The function should be case-insensitive, ignoring differences in uppercase and lowercase letters, and should also ignore non-alphabetic characters when comparing the strings. It should handle strings of any length, including empty strings, and should also handle Unicode characters and special characters.
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
    return sorted_s1 == sorted_s2