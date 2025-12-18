"""
QUESTION:
Write a function `find_longest_substring(s)` that takes a string `s` of lowercase letters as input and returns the starting and ending indices of the longest substring with no repeating letters and a length of at least 2. The length of the input string `s` will not exceed 10,000.
"""

def find_longest_substring(s):
    n = len(s)
    start = 0
    end = 0
    longest_len = 0
    longest_start = 0
    longest_end = 0
    char_dict = {}

    while end < n:
        if s[end] in char_dict:
            start = max(start, char_dict[s[end]] + 1)
        char_dict[s[end]] = end
        if end - start + 1 > longest_len and end - start + 1 >= 2:
            longest_len = end - start + 1
            longest_start = start
            longest_end = end
        end += 1

    return longest_start, longest_end