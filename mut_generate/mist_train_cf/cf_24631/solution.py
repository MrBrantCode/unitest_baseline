"""
QUESTION:
Write a function `find_longest_at_length` that takes a list of strings `lst` and an integer `k` as input, and returns the longest string in `lst` with a length of `k` or less. If there are multiple longest strings, any one of them can be returned.
"""

def find_longest_at_length(lst, k):
    longest_str = ''
    for s in lst:
        if len(s) <= k and len(s) > len(longest_str):
            longest_str = s
    return longest_str