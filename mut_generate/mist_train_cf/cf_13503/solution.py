"""
QUESTION:
Create a function named `extract_and_sort` that takes a text block as input, extracts all the strings that match the regex pattern "name #number" where the name can be any alphanumeric characters and the number is a 4-digit integer, and returns them in a list sorted in ascending order based on the number. The output should be a list of strings in the format "name #number".
"""

import re

def extract_and_sort(text_block):
    """
    Extracts all the strings that match the regex pattern "name #number" 
    where the name can be any alphanumeric characters and the number is a 4-digit integer, 
    and returns them in a list sorted in ascending order based on the number.

    Args:
        text_block (str): The text block to extract the strings from.

    Returns:
        list: A list of strings in the format "name #number" sorted in ascending order based on the number.
    """

    # Extract strings matching the regex pattern
    pattern = r'(\w+)\s#(\d{4})'
    matches = re.findall(pattern, text_block)

    # Sort the extracted strings based on the number
    sorted_strings = sorted(matches, key=lambda x: int(x[1]))

    # Return the sorted strings
    return [f"{match[0]} #{match[1]}" for match in sorted_strings]