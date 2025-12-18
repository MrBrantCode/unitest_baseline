"""
QUESTION:
Write a function `longest_substring_length(s)` that takes a string `s` as input and returns the length of the longest contiguous substring with no repeated characters. The function should have a time complexity of O(n), where n is the length of the string.
"""

def longest_substring_length(s):
    start = 0
    end = 0
    max_length = 0
    seen = set()

    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            max_length = max(max_length, end - start)
        else:
            seen.remove(s[start])
            start += 1

    return max_length