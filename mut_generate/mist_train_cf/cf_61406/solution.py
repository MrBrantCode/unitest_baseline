"""
QUESTION:
Construct a function called `sequence_check` that determines if a given character sequence starts with the letter 'a' and ends with the letter 'b', regardless of the intervening characters. The function should handle erroneous inputs and edge cases, such as the absence of the letters 'a' or 'b' in the input sequence, non-string inputs, and empty strings. The function should return a boolean value for valid sequences and an error message for invalid inputs.
"""

def sequence_check(sequence):
    """
    Checks if a given character sequence starts with 'a' and ends with 'b'.

    Args:
    sequence (str): Input character sequence.

    Returns:
    bool: True if sequence starts with 'a' and ends with 'b', False otherwise.
    str: Error message if input is not a string or is an empty string.
    """
    # Handle Non-string and None inputs:
    if not isinstance(sequence, str) or sequence is None:
        return "Error: Input is not a string."
    # Handle Empty strings:
    elif len(sequence) == 0:
        return "Error: String is empty."
    else:
        return sequence[0] == 'a' and sequence[-1] == 'b'