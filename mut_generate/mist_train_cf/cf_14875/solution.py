"""
QUESTION:
Write a function named `count_non_printable_characters` that takes an input string and returns a tuple containing the count of non-printable characters and a list of these non-printable characters. A non-printable character is defined as any character that cannot be displayed on the screen, such as control characters, special characters, and whitespace characters. The function should handle multi-line strings and count each non-printable character occurrence separately.
"""

import string

def count_non_printable_characters(input_string):
    non_printable_characters = []
    count = 0
    
    for char in input_string:
        if char not in string.printable:
            count += 1
            non_printable_characters.append(char)
    
    return count, non_printable_characters