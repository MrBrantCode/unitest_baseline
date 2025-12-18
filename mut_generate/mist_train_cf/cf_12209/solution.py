"""
QUESTION:
Design a function `longest_substring_without_repeating_chars` that takes a string `s` as input and returns the longest substring with no repeating characters. The function should be case-sensitive, treating "a" and "A" as different characters, and should work with strings containing spaces and special characters. If there are multiple longest substrings with no repeating characters, any one of them can be returned.
"""

def longest_substring_without_repeating_chars(s):
    result = ""
    char_map = {}
    start = 0
    end = 0

    while end < len(s):
        if s[end] not in char_map or char_map[s[end]] < start:
            char_map[s[end]] = end
        else:
            start = char_map[s[end]] + 1
            char_map[s[end]] = end

        substring_length = end - start + 1
        if substring_length > len(result):
            result = s[start:end+1]

        end += 1

    return result