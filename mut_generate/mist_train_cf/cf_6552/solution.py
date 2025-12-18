"""
QUESTION:
Write a function called `longest_non_repeating_substring` that takes a string `s` as input and returns the length of the longest consecutive substring of non-repeating characters. The function should consider both uppercase and lowercase characters as distinct and assume that the input string contains only printable ASCII characters.
"""

def longest_non_repeating_substring(s):
    n = len(s)
    max_len = 0
    start = 0
    seen = {}

    for end in range(n):
        if s[end] in seen:
            start = max(start, seen[s[end]] + 1)
        seen[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len