"""
QUESTION:
Write a function named `extract_substrings` that extracts all substrings from a given string that match the pattern "AAA_BBB_CCC" and are immediately followed by either "DDD" or "EEE". The function should return a list of the matched substrings.
"""

import re

def extract_substrings(s):
    """
    Extracts all substrings from a given string that match the pattern "AAA_BBB_CCC" 
    and are immediately followed by either "DDD" or "EEE".
    
    Args:
        s (str): The input string.
    
    Returns:
        list: A list of the matched substrings.
    """
    pattern = r"(?:AAA_BBB_CCC)(?:DDD|EEE)"
    return re.findall(pattern, s)