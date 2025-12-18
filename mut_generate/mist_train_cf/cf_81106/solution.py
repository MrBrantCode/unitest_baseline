"""
QUESTION:
Design a function `is_legit_postcode` that checks if a given string represents a valid UK Royal Mail postcode. A valid postcode is an alphanumeric string of five to seven characters divided into two parts by a single space, where the first part (out code) has two to four characters, and the second part (in code) has three characters. The function should return True if the postcode is valid and False otherwise.
"""

import re

def is_legit_postcode(postcode):
    pattern = r"^(GIR 0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9]|[ABEHMNPRVWXY]))|[0-9][A-HJKPS-UW]) [0-9][ABD-HJLNP-UW-Z]{2})$"
    return bool(re.search(pattern, postcode))