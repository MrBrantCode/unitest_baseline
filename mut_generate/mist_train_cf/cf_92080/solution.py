"""
QUESTION:
Write a function `longest_run(string)` that returns the length of the longest run of consecutive characters in the given string. The function should consider a run as a sequence of consecutive characters that are the same.
"""

def longest_run(string):
    max_length = 0
    current_length = 0
    current_char = None

    for char in string:
        if char == current_char:
            current_length += 1
        else:
            current_char = char
            current_length = 1

        max_length = max(max_length, current_length)

    return max_length