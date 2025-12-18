"""
QUESTION:
Write a function `count_non_printable_characters` that takes a string as input and returns a tuple containing the total count of non-printable characters and a dictionary where keys are unique non-printable characters and values are their respective counts. The function should handle strings with a length of up to 1 million characters efficiently.
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