"""
QUESTION:
Design a function named `validate_phone_number` that takes a string `num` as input and returns a string indicating whether the phone number is valid or not. The function should validate phone numbers from multiple international formats, including the United States, United Kingdom, and Germany. The function should return 'The phone number [num] is valid' if the number matches any of the recognized formats, and 'The phone number [num] is not valid' otherwise.
"""

import re

def validate_phone_number(num):
    # regular expression patterns for various international phone numbers
    patterns = [
        '^1[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$',  # United States
        '^\+44[-\s]?\d{2}[-\s]?\d{4}[-\s]?\d{4}$',     # United Kingdom
        '^0\d{2,4}[-\s]?\d{6,8}$',                      # United Kingdom (Local)
        '^\+49[-\s]?\d{3}[-\s]?\d{7,8}$',               # Germany
        '^0\d{10,11}$'                                  # Germany (Local)
    ]

    # check each pattern
    for pattern in patterns:
        if re.match(pattern, num):
            return 'The phone number '+ num + ' is valid'
            
    # if no pattern matches, return an error
    return 'The phone number '+ num + ' is not valid'