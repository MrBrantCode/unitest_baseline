"""
QUESTION:
Write a function `is_anagram(s1, s2)` that determines if string `s1` is an anagram of string `s2` by ignoring case sensitivity and non-alphabetic characters, and returns a boolean value.
"""

def is_anagram(s1, s2):
    # Convert both strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Remove non-alphabetic characters
    s1 = ''.join(ch for ch in s1 if ch.isalpha())
    s2 = ''.join(ch for ch in s2 if ch.isalpha())
    
    # Sort the characters in both strings
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    
    # Compare the sorted strings
    return s1 == s2