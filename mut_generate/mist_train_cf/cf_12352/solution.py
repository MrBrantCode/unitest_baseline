"""
QUESTION:
Write a function `longest_substring_without_repeating_characters` that takes a string as input and returns the longest substring without repeating characters. If multiple substrings with the same length exist, return the first occurring one. Assume the input string contains only lowercase English letters and the function is case-sensitive. The function should handle empty strings and strings with a length of 1 appropriately.
"""

def longest_substring_without_repeating_characters(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s

    start = 0
    end = 0
    max_length = 0
    max_start = 0
    characters = set()

    while end < len(s):
        if s[end] not in characters:
            characters.add(s[end])
            end += 1
            if end - start > max_length:
                max_length = end - start
                max_start = start
        else:
            characters.remove(s[start])
            start += 1

    return s[max_start:max_start+max_length]