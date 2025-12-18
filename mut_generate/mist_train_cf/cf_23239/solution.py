"""
QUESTION:
Write a function named `is_anagram` that takes two strings as parameters and returns a boolean value indicating whether the strings are anagrams of each other, ignoring case and whitespace. The function should return False for strings of different lengths.
"""

def is_anagram(s, t):
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()
    
    if len(s) != len(t): return False
    
    s = sorted(s)
    t = sorted(t)
    
    return s == t