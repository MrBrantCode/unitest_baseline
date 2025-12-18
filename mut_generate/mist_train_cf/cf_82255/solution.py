"""
QUESTION:
Extract the "Description" value from a JSON string using a regular expression. The function should take a JSON string as input and return the value of the "Description" key. The input JSON string may or may not contain a value for the "Description" field. The function should be able to handle cases where the "Description" value is empty or missing.
"""

import re

def extract_description(json_str):
    """
    Extract the "Description" value from a JSON string using a regular expression.

    Args:
        json_str (str): The input JSON string.

    Returns:
        str: The value of the "Description" key, or None if not found.
    """
    pattern = r'"Description":"(.*?)"'
    match = re.search(pattern, json_str)
    if match:
        return match.group(1)
    else:
        return None