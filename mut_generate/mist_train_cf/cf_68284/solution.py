"""
QUESTION:
Write a function called `is_anagram` that takes a string `s` as input and returns a boolean indicating whether the string is an anagram of its reverse, ignoring case, punctuation, spaces, and special characters.
"""

def is_anagram(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]