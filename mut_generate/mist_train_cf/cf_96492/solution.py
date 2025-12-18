"""
QUESTION:
Extract all strings from a given text block in the format "name #number", where the name can be any alphanumeric characters and the number is a 4-digit integer. The extracted strings should be sorted in descending order based on the number. Implement this extraction and sorting using a function named `extract_and_sort`.
"""

import re

def extract_and_sort(text_block):
    """
    Extracts all strings from a given text block in the format "name #number", 
    where the name can be any alphanumeric characters and the number is a 4-digit integer. 
    The extracted strings are sorted in descending order based on the number.

    Args:
        text_block (str): The input text block.

    Returns:
        list: A list of extracted strings sorted in descending order based on the number.
    """

    pattern = r'(\w+) #(\d{4})'  # Regex pattern to match name and number
    matches = re.findall(pattern, text_block)  # Find all matches in the text block
    sorted_matches = sorted(matches, key=lambda x: int(x[1]), reverse=True)  # Sort matches based on number in descending order
    result = [' '.join(match) for match in sorted_matches]  # Convert matches to strings

    return result