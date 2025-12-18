"""
QUESTION:
Create a function named `get_unique_chars` that takes one input parameter. The function should truncate the input string to display only the first 4 unique characters in alphabetical order and output the unique set of characters. If the string has less than four unique characters, it should display the unique characters only. The function must also include error handling for non-string inputs.
"""

def get_unique_chars(in_string):
    if not isinstance(in_string, str):
        return 'Error: Provided input is not a string.'
    unique_chars = sorted(set(in_string))
    return ''.join(unique_chars[:4])