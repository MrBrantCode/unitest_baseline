"""
QUESTION:
Write a function named `is_anagram` that takes two strings as input and returns a boolean indicating whether they are anagrams while ignoring case and non-alphabetic characters. The function should consider 'A' and 'a' as the same character and should ignore spaces and punctuation.
"""

def is_anagram(s1, s2):
    s1 = ''.join(ch.lower() for ch in s1 if ch.isalpha())
    s2 = ''.join(ch.lower() for ch in s2 if ch.isalpha())
    return sorted(s1) == sorted(s2)