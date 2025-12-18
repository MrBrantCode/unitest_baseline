"""
QUESTION:
Write a function named `reverse_string` that takes a string `s` as input and returns the reversed string, considering consecutive whitespace characters as a single whitespace character. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions or data structures.
"""

def reverse_string(s):
    chars = list(s)
    start = 0
    end = len(chars) - 1

    while start < end:
        if chars[start].isspace():
            while start < end and chars[start].isspace():
                start += 1

        if chars[end].isspace():
            while start < end and chars[end].isspace():
                end -= 1

        chars[start], chars[end] = chars[end], chars[start]

        start += 1
        end -= 1

    return ''.join(chars)