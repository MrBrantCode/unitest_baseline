"""
QUESTION:
Write a function called `longest_substring_length` that takes a string `s` as input and returns the length of the longest substring without repeating characters. The function must have a time complexity of O(n).
"""

def longest_substring_length(s):
    last_index = {}
    start_index = 0
    max_length = 0

    for i in range(len(s)):
        if s[i] in last_index and last_index[s[i]] >= start_index:
            start_index = last_index[s[i]] + 1

        last_index[s[i]] = i
        max_length = max(max_length, i - start_index + 1)

    return max_length