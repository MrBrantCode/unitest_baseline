"""
QUESTION:
Write a function `longest_substring_without_repeating_chars(s)` that finds the longest substring with no repeating characters in a given string `s`. The function should consider the input string as case-sensitive and return any one of the longest substrings if there are multiple. The input string may contain both lowercase and uppercase letters, spaces, and special characters.
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