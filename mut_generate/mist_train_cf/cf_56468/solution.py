"""
QUESTION:
Create a regular expression that verifies the authenticity of a USA phone number. The regex should account for the optional inclusion of the country code (+1 or 1) and various formatting patterns, such as the use of parentheses for the area code and the separation of digit groups by space, dot, or hyphen.
"""

import re

def validate_phone_number(phone_number):
    pattern = r"^(?:\+?1[-.\s]?)?(?:\((\d{3})\)|(\d{3}))[-.\s]?(\d{3})[-.\s]?(\d{4})$"
    return bool(re.match(pattern, phone_number))