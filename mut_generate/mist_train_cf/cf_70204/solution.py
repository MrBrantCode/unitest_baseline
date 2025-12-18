"""
QUESTION:
Given two strings `s` and `t`, write a function `isAnagram` that returns `true` if `t` is an anagram of `s`, and `false` otherwise. The comparison should be case-sensitive and special characters should be considered. The function should be able to handle strings consisting of any printable ASCII characters with a length between 1 and 5 * 10^4.
"""

from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)