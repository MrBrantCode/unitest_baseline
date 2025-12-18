"""
QUESTION:
Write a function named `longest_substring_without_repeated_chars` that takes a string as input and returns the longest substring without any repeated characters. If there are multiple substrings of the same length, return the one that appears first in the original string.
"""

def longest_substring_without_repeated_chars(string):
    start = 0
    end = 0
    max_len = 0
    max_start = 0
    max_end = 0
    char_set = set()

    while end < len(string):
        if string[end] not in char_set:
            char_set.add(string[end])
            end += 1
        else:
            if (end - start) > max_len:
                max_len = end - start
                max_start = start
                max_end = end
            start += 1
            char_set.clear()

    if (end - start) > max_len:
        max_start = start
        max_end = end

    return string[max_start:max_end]