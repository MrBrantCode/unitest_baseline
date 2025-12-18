"""
QUESTION:
Write a function `find_separated_by_semi_colon(txt)` that takes a string input `txt` and returns a list of substrings separated by semicolons. The function should return an error message "Error: The input must be a string" if the input is not a string. The function should use a regular expression to find all instances of substrings separated by semicolons.
"""

import re

def find_separated_by_semi_colon(txt):
    if not isinstance(txt, str):
        return "Error: The input must be a string"
        
    pattern = r'[^;]+' 
    matches = re.findall(pattern, txt)
    return matches