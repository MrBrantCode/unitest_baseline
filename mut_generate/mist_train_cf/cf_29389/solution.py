"""
QUESTION:
Implement a function `findLongestSubstring(s: str) -> int` that takes a string `s` consisting of lowercase English letters as input and returns the length of the longest substring of `s` that contains at most two distinct characters.
"""

def findLongestSubstring(s: str) -> int:
    if len(s) < 3:
        return len(s)

    max_length = 0
    left = 0
    right = 0
    char_map = {}

    while right < len(s):
        char_map[s[right]] = right
        if len(char_map) > 2:
            min_index = min(char_map.values())
            left = min_index + 1
            del char_map[s[min_index]]
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length