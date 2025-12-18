"""
QUESTION:
Write a function `is_substring(s1: str, s2: str) -> bool` that returns True if s2 is a substring of s1 and False otherwise, given two strings s1 and s2. Both strings will only contain lowercase letters and their lengths will be at most 10^5.
"""

def entrance(s1: str, s2: str) -> bool:
    return s2 in s1