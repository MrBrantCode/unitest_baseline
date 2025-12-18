"""
QUESTION:
Write a function called `is_anagram` that takes two strings as input and returns a boolean indicating whether the strings are anagrams of each other. The comparison should be case-insensitive and ignore non-alphanumeric characters.
"""

def is_anagram(s, t):
    s = s.lower()
    t = t.lower()
    
    s = ''.join(e for e in s if e.isalnum())
    t = ''.join(e for e in t if e.isalnum())
    
    s = sorted(s)
    t = sorted(t)
    
    return s == t