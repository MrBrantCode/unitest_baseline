"""
QUESTION:
Write a function `longest_substring_length(s: str) -> int` that takes a string `s` consisting of lowercase English letters as input and returns the length of the longest substring without repeating characters. The function should have a time complexity of O(n), where n is the length of the input string `s`.
"""

def longest_substring_length(s: str) -> int:
    if not s:
        return 0
    max_length = 0
    start = 0
    char_index_map = {}

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        char_index_map[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length