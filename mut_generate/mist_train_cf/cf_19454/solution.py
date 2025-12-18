"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks if two strings are anagrams, considering both uppercase and lowercase letters, as well as special characters and numbers. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def is_anagram(s1, s2):
    s1 = ''.join(e for e in s1 if e.isalnum()).lower()
    s2 = ''.join(e for e in s2 if e.isalnum()).lower()
    return sorted(s1) == sorted(s2)