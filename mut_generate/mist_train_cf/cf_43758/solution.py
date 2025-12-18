"""
QUESTION:
Create a function `extract_pattern` that takes a string as input and returns all substrings that match the pattern "AAA_BBB_CCC", where "AAA", "BBB", and "CCC" are alphanumeric strings with at least one lowercase letter, one uppercase letter, and one digit.
"""

import re

def extract_pattern(input_string):
    """
    Extracts substrings from the input string that match the pattern "AAA_BBB_CCC",
    where "AAA", "BBB", and "CCC" are alphanumeric strings with at least one lowercase 
    letter, one uppercase letter, and one digit.
    
    Args:
    input_string (str): The input string to search for the pattern.
    
    Returns:
    list: A list of substrings that match the pattern.
    """

    # Define the regular expression pattern
    pattern = r"(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]+_(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]+_(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)[a-zA-Z\d]+"
    
    # Find all matches of the pattern in the input string
    matches = re.findall(pattern, input_string)
    
    return matches