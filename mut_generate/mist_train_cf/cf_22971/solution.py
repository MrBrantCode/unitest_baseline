"""
QUESTION:
Write a function called `count_non_printable_characters` that takes a single string argument `input_string` and returns the total count of non-printable characters in the string and a dictionary of non-printable characters with their respective counts. The function should consider non-printable characters as any character that is not in the `string.printable` string. It should handle strings with a length of up to 1 million characters efficiently and count each non-printable character occurrence separately, including in multi-line strings.
"""

import string

def count_non_printable_characters(input_string):
    non_printable_characters = {}
    count = 0

    for char in input_string:
        if char not in string.printable:
            if char not in non_printable_characters:
                non_printable_characters[char] = 1
            else:
                non_printable_characters[char] += 1
            count += 1

    return count, non_printable_characters