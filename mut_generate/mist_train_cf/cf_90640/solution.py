"""
QUESTION:
Write a function `find_longest_string` that takes a list of strings as input and returns the longest string without using any built-in string manipulation functions or sorting algorithms.
"""

def find_longest_string(strings):
    longest = ""
    for string in strings:
        length = 0
        for char in string:
            length += 1
        if length > len(longest):
            longest = string
    return longest