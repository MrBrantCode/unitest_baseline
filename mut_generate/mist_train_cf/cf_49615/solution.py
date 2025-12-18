"""
QUESTION:
Implement a function `intricate_string_alteration(input_string)` that takes a string as input and returns a transformed string. The transformation involves three steps: 
1. Replace each single space with an underscore.
2. Replace two or more consecutive spaces (or underscores) with a single hyphen.
3. Convert all words in the string to uppercase.

The function should handle edge cases such as leading, trailing, or multiple consecutive spaces.
"""

import re

def intricate_string_alteration(input_string):
    input_string = input_string.replace(' ', '_')      # replace all single spaces with underscore.
    input_string = re.sub(r'_{2,}', '-', input_string) # replace all 2 or more consecutive underscores with 1 hyphen.
    input_string = input_string.upper()                # convert all words to uppercase.
    return input_string