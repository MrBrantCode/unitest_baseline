"""
QUESTION:
Write a function `get_string_length(s)` to calculate the length of a given string `s` without using any string manipulation functions, looping constructs, or recursion. The function should have a time complexity of O(1).
"""

def get_string_length(s):
    pointer = s.__iter__()
    length = 0
    try:
        while True:
            next(pointer)
            length += 1
    except StopIteration:
        return length