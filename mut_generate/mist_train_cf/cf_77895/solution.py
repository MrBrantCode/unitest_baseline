"""
QUESTION:
Construct a regular expression to match a phone number in the format (123) 456-7890, where the phone number consists of a three-digit area code enclosed in parentheses, followed by a space, then three more digits, a hyphen, and finally four digits.
"""

def validate_phone_number(phone_number):
    import re
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')
    return bool(pattern.match(phone_number))