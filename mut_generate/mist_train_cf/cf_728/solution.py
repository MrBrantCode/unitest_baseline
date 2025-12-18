"""
QUESTION:
Write a function named `convert_to_string` that takes a list of characters as input, removes any leading or trailing whitespace characters from the resulting string, replaces any consecutive whitespace characters within the input list with a single whitespace character, and preserves the original order of the characters in the input list. The function should handle cases where the input list is empty, contains only whitespace characters, or contains non-ASCII characters.
"""

import unicodedata

def convert_to_string(char_list):
    if len(char_list) == 0 or all(c.isspace() for c in char_list):
        return ""
    
    string = "".join(char_list)
    string = string.strip()
    string = " ".join(string.split())
    string = unicodedata.normalize("NFKD", string)
    
    # Remove checks for specific character sets as per original question constraints
    return string