"""
QUESTION:
Write a function `remove_punctuation_and_numbers` that takes a string as input and returns the string with all punctuation and numbers removed. The function should not use any external libraries.
"""

def remove_punctuation_and_numbers(input_string):
    """
    This function removes all punctuation and numbers from a given string.

    Parameters:
    input_string (str): The input string from which punctuation and numbers will be removed.

    Returns:
    str: The input string with all punctuation and numbers removed.
    """

    # Initialize an empty string to store the result
    result = ""

    # Iterate over each character in the input string
    for char in input_string:
        # Check if the character is a letter or a space
        if char.isalpha() or char.isspace():
            # If the character is a letter or a space, add it to the result
            result += char

    # Return the result
    return result