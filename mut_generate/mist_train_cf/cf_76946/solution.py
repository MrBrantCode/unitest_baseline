"""
QUESTION:
Write a function `longest_distinct_substring(s)` that finds the longest substring(s) of a given string `s` with distinct characters and returns their starting and ending indices. If multiple substrings of equal maximum length exist, return all of them.
"""

def longest_distinct_substring(s):
    n = len(s)
    substrings = []

    max_len = 0
    start = 0
    char_map = {}

    for end in range(n):
        if s[end] not in char_map:
            char_map[s[end]] = True
        else:
            while s[end] in char_map:
                del char_map[s[start]]
                start += 1
            char_map[s[end]] = True

        if end - start + 1 > max_len:
            max_len = end - start + 1
            substrings = [(start, end)]
        elif end - start + 1 == max_len:
            substrings.append((start, end))

    return substrings, max_len