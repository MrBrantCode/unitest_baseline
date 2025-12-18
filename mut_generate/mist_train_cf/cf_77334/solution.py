"""
QUESTION:
Create a function named `verify_three_numericals` that takes a string `s` as input and returns a boolean indicating whether the string contains at least three numerical characters. The function should use a regular expression pattern to achieve this.
"""

import re

def verify_three_numericals(s):
    pattern = r'\d.*\d.*\d'
    match = re.search(pattern, s)
    
    if match:
        return True
    return False