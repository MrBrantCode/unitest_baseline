"""
QUESTION:
Write a function called `longest_substring` that takes a string as input and returns the length of the longest substring without any repeated characters.
"""

def longest_substring(s):
    seen = {}
    start = 0
    maxlen = 0

    for i, char in enumerate(s):
        if char in seen:
            start = max(start, seen[char] + 1)
        seen[char] = i
        maxlen = max(maxlen, i - start + 1)

    return maxlen