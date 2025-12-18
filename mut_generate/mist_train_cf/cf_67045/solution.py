"""
QUESTION:
Write a function `maxLengthBetweenEqualCharacters(s)` that takes a string `s` of length between 1 and 300 containing only lowercase English letters, and returns the length of the longest substring between two equal characters, excluding the two characters. If no such substring exists, return -1. The substring should not contain any repeating characters. If multiple substrings satisfy the conditions, return the length of the substring that occurs first.
"""

def maxLengthBetweenEqualCharacters(s):
    max_length = -1
    char_positions = {}
    for i, char in enumerate(s):
        if char in char_positions:
            j = char_positions[char]
            substring = s[j+1:i]
            if len(substring) == len(set(substring)):
                max_length = max(max_length, len(substring))
        else:
            char_positions[char] = i
    return max_length