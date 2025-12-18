"""
QUESTION:
Write a function `match_text(input_text)` that strictly matches strings encapsulating an exact sequence of three uppercase letters followed by two lowercase letters in the given `input_text`. The function should exclude any sequences where the three uppercase letters are all identical and return all valid matches. If no matches are found, return "No Match Found".
"""

import re

def match_text(input_text):
    reg_ex = r'\b(?!([A-Z])\1{2})[A-Z]{3}[a-z]{2}\b'
    matches = re.findall(reg_ex, input_text)
    return matches if matches else "No Match Found"