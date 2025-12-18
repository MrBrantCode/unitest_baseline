"""
QUESTION:
Implement a function `longest_substring(s)` that takes a string `s` as input and returns the length of the longest substring without repeating characters. The function should have a time complexity of O(n) and only use a constant amount of extra space.
"""

def longest_substring(s):
    n = len(s)
    max_len = 0
    left = 0
    chars = set()

    for right in range(n):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len