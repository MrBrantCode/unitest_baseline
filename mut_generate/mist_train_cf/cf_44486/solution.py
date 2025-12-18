"""
QUESTION:
Create a function named `remove_duplicates` that takes a string as input and returns a new string with all duplicate characters removed, while preserving the original order of distinct elements.
"""

def remove_duplicates(input_string):
    result = ''
    for char in input_string:
        if char not in result:
            result += char
    return result