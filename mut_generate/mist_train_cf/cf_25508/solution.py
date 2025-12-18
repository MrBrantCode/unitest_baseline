"""
QUESTION:
Write a function `longest_consecutive_str(s)` that takes a string `s` as input and returns the longest consecutive character string in `s`. The function should return the first longest consecutive string it encounters in case of a tie.
"""

def longest_consecutive_str(s):
    longest_str = ""
    cur_str = ""

    for char in s:
        if not cur_str or char == cur_str[-1]:
            cur_str += char
        else:
            if len(cur_str) > len(longest_str):
                longest_str = cur_str
            cur_str = char

    if len(cur_str) > len(longest_str):
            longest_str = cur_str

    return longest_str