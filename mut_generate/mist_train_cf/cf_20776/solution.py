"""
QUESTION:
Create a regular expression for the function `match_number` that matches all numbers of the form 1xx-xxx-xxxx, where xx cannot be greater than 50 and the last digit of the number must be odd. The regular expression should ensure that the number is not part of a larger word.
"""

import re

def match_number(s):
    pattern = r'\b1[0-5][0-9]-\d{3}-\d*[13579]\b'
    return bool(re.match(pattern, s))