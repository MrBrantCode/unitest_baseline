"""
QUESTION:
Create a function called `process_string` that takes a string as input. The function should convert all alphabetical characters to lowercase, ignore any non-alphabetical characters, remove any duplicate characters, and sort the resulting string in alphabetical order. The input string may contain a mix of uppercase and lowercase letters, numbers, and special characters.
"""

import re

def process_string(input_str):
    """
    This function processes a given string by converting it to lowercase, 
    removing non-alphabetical characters, removing duplicates, and sorting it.
    
    Args:
        input_str (str): The input string to be processed.
    
    Returns:
        str: The processed string.
    """
    # Remove special characters and numbers from the string
    string = re.sub(r'[^a-zA-Z\s]', '', input_str)
    
    # Convert the string to lowercase
    string = string.lower()
    
    # Remove duplicate characters
    string = "".join(set(string))
    
    # Sort the resulting string in alphabetical order
    string = "".join(sorted(string))
    
    return string