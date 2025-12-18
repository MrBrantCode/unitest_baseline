"""
QUESTION:
Write a function `convert_string_to_floats` that takes a string input within square brackets and converts it into a list of floats. The input string may contain invalid characters, extra spaces, multiple strings with similar format within the brackets, or be in an invalid format. The function should handle these cases by removing invalid characters, ignoring extra spaces, combining multiple strings into one list of floats, and returning an error message for invalid input formats.
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