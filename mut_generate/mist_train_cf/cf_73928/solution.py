"""
QUESTION:
Create a function named `validate_imeisv` that takes a string as input and returns a boolean indicating whether the string matches the format of an IMEISV number, which consists of exactly 16 digits.
"""

import re

def validate_imeisv(imeisv):
    imeisv_pattern = re.compile(r'^\d{16}$') 
    if imeisv_pattern.match(imeisv): 
        return True
    else:
        return False