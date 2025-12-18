"""
QUESTION:
Create a function named `checkPhoneNumber` that takes two parameters: `phone` (a string representing a phone number) and `areaCodes` (a list of predetermined area codes). The function should return `True` if the phone number matches the standard American telephone number format and its area code is found in the `areaCodes` list. Otherwise, it should return `False`. The area code should be the first three digits of the phone number, and the function should only check the 10-digit format for American phone numbers, excluding country codes or international prefixes.
"""

import re

def checkPhoneNumber(phone, areaCodes):
    # check American phone number pattern
    pattern = re.compile(r'\(?([2-9]{1}[0-9]{2})\)?[-. ]?([2-9]{1}[0-9]{2})[-. ]?([0-9]{4})$')
    match = pattern.match(phone)

    # if the phone number matches the pattern
    if match:
        # check area code
        areaCode = match.group(1)
        if areaCode in areaCodes:
            return True
        else:
            return False
    else:
        return False