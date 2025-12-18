"""
QUESTION:
Compare the two input strings character by character and return the number of matching characters that are lowercase alphabets. The function should be named "compare_strings" and should take two parameters, string1 and string2. The function should check if the lengths of string1 and string2 are equal and return an error message if they are not.
"""

import re

def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return "Error: Strings should be of equal length"
    count = 0
    for char1, char2 in zip(string1, string2):
        if char1 == char2 and re.match("^[a-z]+$", char1):
            count += 1
    return count