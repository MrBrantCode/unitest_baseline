"""
QUESTION:
Design a function named `remove_punctuation` that takes two parameters, `input_string` and `punctuation`, and returns a string with all occurrences of the specified `punctuation` removed from the `input_string`, while preserving the positions of other characters. The `punctuation` parameter should be a single character.
"""

def remove_punctuation(input_string, punctuation):
    """
    Removes all occurrences of a specified punctuation mark from a given string.

    Args:
    input_string (str): The original string from which the punctuation should be removed.
    punctuation (str): The specific punctuation mark to be removed.

    Returns:
    str: The modified string with the specified punctuation mark removed.
    """
    output_string = ""
    for char in input_string:
        if char not in punctuation:
            output_string += char
    return output_string