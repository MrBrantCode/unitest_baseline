"""
QUESTION:
Write a function called `find_longest_string` that takes a list of strings as input and returns the longest string. You cannot use any built-in string manipulation functions or sorting algorithms to find the length of the strings or to compare their lengths.
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