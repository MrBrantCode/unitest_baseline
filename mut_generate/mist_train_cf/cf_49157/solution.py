"""
QUESTION:
Write a REGEXTRACT function to extract a street address that is followed by either a comma (",") or the word "between". The function should match up to the first instance of either character/string without including the comma or "between" in the match.
"""

import re

def REGEXTRACT(address):
    """
    Extracts a street address that is followed by either a comma (",") or the word "between".
    
    Args:
    address (str): The input string containing the address.

    Returns:
    str: The extracted address.
    """
    pattern = r"^(.*?)(?=,| between)"
    match = re.search(pattern, address)
    if match:
        return match.group(0)
    else:
        return None