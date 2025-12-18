"""
QUESTION:
Implement the `remove_trailing_spaces` function, which takes a string as input and returns the string with all trailing spaces removed. The input string may contain alphanumeric characters, spaces, and punctuation. You cannot use any built-in string functions or libraries.
"""

def remove_trailing_spaces(input_string):
    # Start from the end of the string
    i = len(input_string) - 1
    # Iterate until a non-space character is found or we reach the beginning of the string
    while i >= 0 and input_string[i] == ' ':
        i -= 1
    # Return the substring without trailing spaces
    return input_string[:i+1]