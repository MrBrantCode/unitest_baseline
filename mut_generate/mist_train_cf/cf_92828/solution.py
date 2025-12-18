"""
QUESTION:
Write a function `extract_sorted_strings` that takes a text block as input and returns a list of strings in the format "name #number", where the name can be any alphanumeric characters and the number is a 4-digit integer. The strings should be sorted in ascending order based on the number.
"""

import re

def extract_sorted_strings(text_block):
    """
    Extracts strings in the format "name #number" from a text block and returns them in a sorted list.
    
    Args:
        text_block (str): The input text block.
    
    Returns:
        list: A list of strings in the format "name #number", sorted in ascending order based on the number.
    """
    # Extract strings matching the regex pattern
    pattern = r'(\w+)\s#(\d{4})'
    matches = re.findall(pattern, text_block)

    # Sort the extracted strings based on the number
    sorted_strings = sorted(matches, key=lambda x: int(x[1]))

    # Return the sorted strings in the format "name #number"
    return [f"{match[0]} #{match[1]}" for match in sorted_strings]