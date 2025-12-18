"""
QUESTION:
Develop a function named `replace_non_alpha_numeric` that takes two parameters: `text` and `replacement`. The function should substitute all non-alphanumeric characters (excluding whitespace) in `text` with the `replacement` symbol. If a non-alphanumeric character is surrounded by `replacement` symbols, it should be discarded instead of adding another `replacement` symbol. Additionally, no two `replacement` symbols should be adjacent to each other.
"""

import re

def replace_non_alpha_numeric(text, replacement):
    # Regular expression for non-alphanumeric characters
    regex = r'\W+'
    new_text = re.sub(regex, replacement, text)
    
    # remove repetition of replacement symbols
    while replacement+replacement in new_text:
        new_text = new_text.replace(replacement+replacement, replacement)
        
    return new_text