"""
QUESTION:
Write a function `longest_run(string)` that returns the length of the longest run of consecutive characters in the input string. A run is a sequence of consecutive characters that are the same. The function should only consider the characters in the input string and return the maximum length of consecutive characters.
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