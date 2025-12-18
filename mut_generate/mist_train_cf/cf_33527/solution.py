"""
QUESTION:
Write a function `longestSubstringLength` that takes a string `s` containing only lowercase English letters and returns the length of the longest substring without repeating characters. The function should be able to handle strings of any length and should return 0 if the input string is empty. The function signature should be `def longestSubstringLength(s: str) -> int`.
"""

def longestSubstringLength(s: str) -> int:
    max_length = 0
    start = 0
    char_index = {}

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length