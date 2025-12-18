"""
QUESTION:
Write a function `longestSubstring` that takes a string `s` consisting of lowercase English letters as input and returns the length of the longest substring that contains at most two distinct characters. 

The function should only consider substrings with a maximum of two distinct characters and return the length of the longest such substring.
"""

def longestSubstring(s: str) -> int:
    if len(s) < 3:
        return len(s)

    max_length = 0
    left = 0
    char_map = {}

    for right in range(len(s)):
        char_map[s[right]] = right
        if len(char_map) == 3:
            del_idx = min(char_map.values())
            left = del_idx + 1
            del char_map[s[del_idx]]

        max_length = max(max_length, right - left + 1)

    return max_length