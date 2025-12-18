"""
QUESTION:
Write a function `check_similarity` that takes two strings as input, `string1` and `string2`. The function should check if both strings only contain lowercase letters from 'a' to 'z'. If they do, it should calculate and return the degree of similarity between the two strings as a float in the range [0,1]. If either string does not meet the criteria, the function should return an error message.
"""

import re
from difflib import SequenceMatcher

def check_similarity(string1, string2):
    pattern = "^[a-z]+$"
    
    # Check if strings comply with the regex
    if re.match(pattern, string1) and re.match(pattern, string2):
        # Calculate similarity
        similarity = SequenceMatcher(None, string1, string2).ratio()
        return similarity
    else:
        return "One or both of the strings do not comply with the regex schematic"