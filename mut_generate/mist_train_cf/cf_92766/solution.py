"""
QUESTION:
Create a function called `is_anagram` that takes two strings as input and returns a boolean indicating whether the strings are anagrams of each other, ignoring case and non-alphabetic characters.
"""

def is_anagram(string1, string2):
    string1 = ''.join(ch.lower() for ch in string1 if ch.isalpha())
    string2 = ''.join(ch.lower() for ch in string2 if ch.isalpha())
    return sorted(string1) == sorted(string2)