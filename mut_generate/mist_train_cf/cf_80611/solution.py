"""
QUESTION:
Create a function `reverse_string` that takes a string and an integer as input. The function should rotate the string by the specified number of characters to the right (positive integer) or left (negative integer) and return the result. The reversal should be performed in a way that handles cases where the reversal value is larger than the length of the string. The input must be validated to ensure it is a string and the reversal value is an integer.
"""

def reverse_string(string, num_chars):
    # Validate input types
    assert isinstance(string, str), "Input must be a string"
    assert isinstance(num_chars, int), "Reversal value must be an integer"

    # Handle reversal values larger than the length of the string
    num_chars %= len(string)

    # Perform reversal
    return string[-num_chars:] + string[:-num_chars]