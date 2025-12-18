"""
QUESTION:
Create a function `inverse_sequence` that takes a string of alphanumeric characters as input and returns the characters in reverse order. The function should handle empty strings and large inputs efficiently, and its execution time should be within a predetermined limit of 1 second for inputs of up to 1 million characters.
"""

def inverse_sequence(s):
    """
    Returns the input string in reverse order.

    Args:
        s (str): A string of alphanumeric characters.

    Returns:
        str: The characters in the input string in reverse order.
    """
    return s[::-1]