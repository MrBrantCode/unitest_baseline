"""
QUESTION:
Write a function `convert_string_to_floats` that takes a string as input, where the string contains a list of numbers enclosed in square brackets and separated by spaces. The function should convert the string into a list of floats, handling the following cases: 

- If the string contains invalid characters, such as alphabets or special characters, remove those characters and convert the remaining string into a list of floats.
- If the string contains missing or extra spaces between numbers, remove the extra spaces and convert the remaining string into a list of floats.
- If the string contains multiple strings with similar format within square brackets, convert each individual string into a list of floats and combine them into a single list of floats.
- If the input is not in the correct format, return an error message indicating the specific issue with the input.

The input string is guaranteed to be a string within square brackets, but the content of the string may vary and needs to be handled accordingly.
"""

import re

def convert_string_to_floats(string):
    # Remove the square brackets from the input string
    string = string.strip("[]")

    # Split the string into individual strings based on the spaces
    strings = re.split(r'\s+', string)

    # Initialize the final list of floats
    floats = []

    # Iterate over each individual string
    for s in strings:
        try:
            # Convert the string to a float and append it to the final list
            floats.append(float(s))
        except ValueError:
            # If the string contains invalid characters, remove them and convert the remaining string into a float
            s = re.sub(r'[^0-9.]+', '', s)
            try:
                floats.append(float(s))
            except ValueError:
                # If the string cannot be converted into a float, return an error message
                return f"Invalid format: '{s}' is not a valid number"

    return floats