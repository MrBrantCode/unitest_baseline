"""
QUESTION:
Write a function named `convert_to_string` that takes a list of characters as input and returns a string. The function should handle cases where the input list is empty or contains only whitespace characters, and should remove any leading or trailing whitespace characters from the resulting string. Consecutive whitespace characters within the input list should be replaced with a single whitespace character in the resulting string. The function should also preserve the original order of the characters in the input list and handle non-ASCII characters correctly.
"""

import unicodedata
import string

def convert_to_string(char_list):
    # Check if the input list is empty or contains only whitespace characters
    if len(char_list) == 0 or all(c.isspace() for c in char_list):
        return ""
    
    # Convert the list of characters to a string
    result = "".join(char_list)
    
    # Remove leading and trailing whitespace characters
    result = result.strip()
    
    # Replace consecutive whitespace characters with a single whitespace character
    result = " ".join(result.split())
    
    # Normalize the string to handle non-ASCII characters
    result = unicodedata.normalize("NFKD", result)
    
    return result