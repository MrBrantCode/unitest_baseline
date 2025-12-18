"""
QUESTION:
Write a function named `longest_unique_substring` that finds the length of the longest substring with no repeating characters in a given string. The input string can contain any printable ASCII characters and may be extremely large.
"""

def longest_unique_substring(s):
    n = len(s)
    set_chars = set()
    res = float("-inf")
    left = 0
    for right in range(n):
        while s[right] in set_chars:
            set_chars.remove(s[left])
            left += 1
        set_chars.add(s[right])
        res = max(res, right - left + 1)
    return res