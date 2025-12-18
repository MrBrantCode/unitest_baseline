"""
QUESTION:
Create a function `generate_british_hipster_username` that takes a string as input and returns the string if it matches the following conditions: 
- starts with "hip"
- ends with "ster"
- contains at least one of the following words: "tea", "vinyl", "beard", "tweed", "glasses", or "vegan"
- can have any number of characters in between "hip" and "ster" 
using Python's regular expressions.
"""

import re

def generate_british_hipster_username(input_string):
    pattern = r"^hip(.*)(tea|vinyl|beard|tweed|glasses|vegan)ster$"
    match = re.search(pattern, input_string)
    if match:
        return match.group(0)
    else:
        return "No match found."