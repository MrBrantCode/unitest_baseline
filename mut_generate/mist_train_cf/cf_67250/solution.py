"""
QUESTION:
Define a function `longest_string(input_string)` that finds the longest contiguous subset of the same characters within the provided text string and returns this subset. For example, given "Hello, world!", the function should return "ll" because it is the longest sequence of the same characters. The function should only consider contiguous sequences and ignore non-contiguous sequences of the same characters.
"""

def longest_string(input_string):
    max_length = 0
    max_string = ''
    i = 0
    while i < len(input_string):
        curr_length = 1
        curr_string = input_string[i]
        while i + 1 < len(input_string) and input_string[i] == input_string[i+1]:
            i += 1
            curr_length += 1
        if curr_length > max_length:
            max_length = curr_length
            max_string = curr_string
        i += 1
    return max_string * max_length