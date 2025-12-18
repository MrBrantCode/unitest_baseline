"""
QUESTION:
Write a function `format_phone_number` that formats a given phone number, including international numbers and extension numbers. The function should identify the country code and format the number accordingly. It should handle a variety of input formats and return the formatted number as a string.

The function should be able to handle different lengths of phone numbers, including 10, 11, 12, and 13 digits, and format them according to the following rules:

- 10 digits: (XXX) XXX-XXXX (US without country code)
- 11 digits: +X (XXX) XXX-XXXX (US with country code)
- 12 digits: +XX XXX XXXXXXX (UK without area code)
- 13 digits: +XX XX XXXXXXXX (UK with area code)

If the input number contains an extension, the function should format it as XXX-XXX-XXXX ext. XXXX.
"""

import re

def format_phone_number(number):
    # Removing formatting
    number = re.sub(r'\D', "", number)

    # If the number contains extension
    if 'x' in number:
        main, ext = number.split('x')
        return '{} ext. {}'.format(format_phone_number(main), ext)

    # Formatting according to the length of the number
    if len(number) == 10:  # US without area code
        formatted = '({}) {}-{}'.format(number[0:3], number[3:6], number[6:])
    elif len(number) == 11:  # US with area code
        formatted = '+{} ({}) {}-{}'.format(number[0], number[1:4], number[4:7], number[7:])
    elif len(number) == 12:  # UK without area code
        formatted = '+{} {} {}'.format(number[0:2], number[2:5], number[5:])
    elif len(number) == 13:  # UK with area code
        formatted = '+{} {} {} {}'.format(number[0:2], number[2:4], number[4:8], number[8:])
    else:
        formatted = number

    return formatted