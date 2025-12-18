"""
QUESTION:
Write a function `longest_substring(s)` that takes a string `s` as input and returns the longest substring with no repeating characters. If there are multiple substrings with the same maximum length, return the substring that appears first in the original string.
"""

def longest_substring(s):
    start = end = max_start = max_len = 0
    seen = set()

    while end < len(s):
        if s[end] in seen:
            seen.remove(s[start])
            start += 1
        else:
            seen.add(s[end])
            end += 1
            curr_len = end - start
            if curr_len > max_len:
                max_len = curr_len
                max_start = start

    return s[max_start:max_start + max_len]