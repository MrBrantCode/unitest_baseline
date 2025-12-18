"""
QUESTION:
Write a function `count_string_characters()` that takes a string as input, removes whitespace characters, and returns the length of the string, the number of unique characters, the number of special characters, and the number of digits. The function should consider only alphanumeric characters and special characters, ignoring whitespace characters. The function should use Python and utilize built-in string methods.
"""

def count_string_characters(string):
    # Remove whitespace characters from the string
    string = string.replace(" ", "")

    # Initialize variables to count length and unique characters
    length = len(string)
    unique_chars = set(string)

    # Initialize variables to count special characters and digits
    special_chars = 0
    digits = 0

    # Iterate over each character in the string
    for char in string:
        # Check if the character is a special character
        if not char.isalpha() and not char.isdigit():
            special_chars += 1
        # Check if the character is a digit
        if char.isdigit():
            digits += 1

    # Return the results
    return length, len(unique_chars), special_chars, digits