"""
QUESTION:
# Valid HK Phone Number

## Overview

In Hong Kong, a valid phone number has the format ```xxxx xxxx``` where ```x``` is a decimal digit (0-9).  For example:

## Task

Define two functions, ```isValidHKPhoneNumber``` and ```hasValidHKPhoneNumber```, that ```return```s whether a given string is a valid HK phone number and contains a valid HK phone number respectively (i.e. ```true/false``` values).

If in doubt please refer to the example tests.
"""

import re

def isValidHKPhoneNumber(number: str) -> bool:
    HK_PHONE_NUMBER = r'\d{4} \d{4}'
    return bool(re.match(HK_PHONE_NUMBER + r'\Z', number))

def hasValidHKPhoneNumber(number: str) -> bool:
    HK_PHONE_NUMBER = r'\d{4} \d{4}'
    return bool(re.search(HK_PHONE_NUMBER, number))