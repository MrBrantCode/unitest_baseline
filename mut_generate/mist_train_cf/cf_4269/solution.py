"""
QUESTION:
Write a function `reformat_string` that takes a string of three key-value pairs as input. Each key-value pair is separated by a comma and a space, and each key and value is separated by an equal sign. The function should return a string where the key-value pairs are sorted in alphabetical order based on the keys and each pair is enclosed in parentheses, with a comma and a space as the delimiter between pairs. The keys and values only contain alphanumeric characters.
"""

import re

def reformat_string(input_string):
    """
    Reformat a string of three key-value pairs into a string where the key-value pairs are sorted in alphabetical order based on the keys 
    and each pair is enclosed in parentheses, with a comma and a space as the delimiter between pairs.

    Args:
        input_string (str): A string of three key-value pairs.

    Returns:
        str: A string where the key-value pairs are sorted in alphabetical order based on the keys and each pair is enclosed in parentheses.
    """

    # Separate the string into key-value pairs
    pairs = re.findall(r'\b\w+\=\w+\b', input_string)

    # Sort the key-value pairs based on the keys
    sorted_pairs = sorted(pairs)

    # Format the key-value pairs with parentheses
    formatted_pairs = [f'({pair})' for pair in sorted_pairs]

    # Join the formatted pairs with a comma and space delimiter
    output = ', '.join(formatted_pairs)

    return output