"""
QUESTION:
Create a function `validate_phone_number(phone_number)` that takes a string `phone_number` as input and returns `True` if it matches the standard US phone number format and `False` otherwise. The standard format may include an optional international dialing code at the start (like +1) and can be in the form of (XXX) XXX-XXXX, XXX-XXX-XXXX, or 1 XXX XXX XXXX, with spaces, periods, and hyphens as valid delimiters between numbers. The function should not check whether the phone number actually exists, only its format.
"""

import re

def validate_phone_number(phone_number):
  pattern = re.compile(r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
  
  return bool(pattern.match(phone_number))