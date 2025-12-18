"""
QUESTION:
Write an iterative function `longest_substring` that takes a string `input_string` as an argument and returns the longest continuous segment within the string. A continuous segment is a substring where no character repeats. If there are multiple longest continuous segments, return the first one encountered.
"""

def longest_substring(input_string):
    lo_sub = ''
    sub = ''
    for ch in input_string:
        if ch not in sub:
            sub += ch
            if len(sub) > len(lo_sub):
                lo_sub = sub
        else:
            sub = ch
    return lo_sub