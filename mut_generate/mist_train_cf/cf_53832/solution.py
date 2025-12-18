"""
QUESTION:
Write a function `check_uk_postcode(postcode)` that takes a string `postcode` as input and returns whether it matches the pattern of a valid British postal code. The function should be able to correctly detect codes of varying lengths and component orders. The pattern is as follows: the postcode area is either one or two characters long and is all letters, followed by a postcode district that is one or two digits, or a digit followed by a letter, and optionally a space before the last three characters which consist of a digit and two letters.
"""

import re

def check_uk_postcode(postcode):
    uk_postcode_pattern = r"(^[A-Z]{1,2}[0-9]{1,2}[A-Z]?[ ]?[0-9][A-Z]{2}$)"
    return bool(re.match(uk_postcode_pattern, postcode))