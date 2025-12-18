"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input, reverses the order of alphanumeric characters, and preserves the relative positions of special characters and white spaces without using any built-in string reversal functions or slicing methods in Python.
"""

def reverse_string(s):
    s_list = list(s)
    start = 0
    end = len(s_list) - 1 

    while start < end:
        # if character at start or end is not alphanumeric, ignore it
        if not s_list[start].isalnum():
            start += 1
        elif not s_list[end].isalnum():
            end -= 1
        else:
            # if both characters are alphanumeric, swap them
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start, end = start + 1, end - 1
    
    return ''.join(s_list)